from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('SSPES.db')

    conn.row_factory = sqlite3.Row  # Ermöglicht den Zugriff auf die Datenbankzeilen als Dictionaries

    return conn


@app.route("/")
def homePage():
    return "<p>Home Page</p>"


# soll add und update gleichzeitig sein
@app.route('/updateChoice', methods=['POST'])
def update_choice():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tabelle erstellen, wenn sie noch nicht existiert
    cursor.execute("CREATE TABLE IF NOT EXISTS choice (name TEXT, amount INTEGER)")

    # die übergebenen Daten entgegennehmen
    submitted_choices = request.form.to_dict()
    choice_name = submitted_choices.get('name')
    amount = submitted_choices.get('amount')

    if not choice_name or not amount:
        return "Missing choice_name or amount"
    try:
        amount = int(amount)
    except ValueError:
        return "Amount must be an integer"

    cursor.execute('SELECT * FROM choice WHERE name = ?', (choice_name,))
    row = cursor.fetchone()

    if row:
        new_amount = row['amount'] + amount
        cursor.execute('UPDATE choice SET amount = ? WHERE name = ?', (new_amount, choice_name))
    else:
        cursor.execute('INSERT INTO choice (name, amount) VALUES (?, ?)', (choice_name, amount))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'choice_name': choice_name, 'new_amount': amount})


if __name__ == '__main__':
    app.run(debug=True)
