from flask import Flask, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('SSPES.db')
print("totale Änderungen an der Datenbank:   " + str(connection.total_changes))
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS player_choice (name TEXT, amount INTEGER)")
