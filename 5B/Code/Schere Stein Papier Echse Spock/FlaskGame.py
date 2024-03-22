# https://bigbangtheory.fandom.com/de/wiki/Stein,_Papier,_Schere,_Echse,_Spock
# http://www.samkass.com/theories/RPSSL.html
import json
from enum import Enum
import random
import requests
from flask import Flask, request
import sqlite3

"""
1) Als Terminal-Spiel umsetzen
2) Spielmodi COMP vs PLAYER
3) zähle, wer wie oft gewonnen hat
4) zähle alle gewählten Symbole
5) überlege wie die Daten dauerhaft gespeichert werden könnten
6) biete ein Menü an Spielen, Statistik
"""


class weapon(Enum):
    schere = 1
    stein = 2
    papier = 3
    echse = 4
    spock = 5


who_wins_where = {
    weapon.schere: [weapon.papier, weapon.echse],
    weapon.stein: [weapon.echse, weapon.schere],
    weapon.papier: [weapon.stein, weapon.spock],
    weapon.echse: [weapon.spock, weapon.papier],
    weapon.spock: [weapon.stein, weapon.schere]
}


def get_computer_choice():
    # https://stackoverflow.com/questions/24243500/random-choice-on-enum
    return random.choice(list(weapon))


def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "noone"
    # https://stackoverflow.com/questions/11251709/check-if-item-is-in-an-array-list
    if computer_choice in who_wins_where[player_choice]:
        return "player"
    return "computer"


def save_to_file(data1, data2, playerChoices, computerChoices):
    file = open("game_data.txt", "a")
    playerChoicesString = ""
    computerChoicesString = ""
    for c in playerChoices:
        if (playerChoicesString == ""):
            playerChoicesString = playerChoicesString + c
        else:
            playerChoicesString = playerChoicesString + ";" + c
    for c in computerChoices:
        if (computerChoicesString == ""):
            computerChoicesString = computerChoicesString + c
        else:
            computerChoicesString = computerChoicesString + ";" + c
    file.write("\n" + str(data1) + ";" + str(data2) + "!" + str(playerChoicesString) + "|" + str(computerChoicesString))
    file.close()


def main():
    player_wins = 0
    computer_wins = 0
    player_choices = []
    computer_choices = []
    print("-----------------------------------------------------------------------------")
    print("⛄HERRZLICH WILLKOMMEN BEIM WAHNSINNS-SPIEL SCHERE STEIN PAPIER ECHSE SPOCK!!!!⛄")
    print("✁☝⛺⛽")
    print("-----------------------------------------------------------------------------")
    print("WICHTIG!!! haben Sie den Flask Server gestartet??? -> Flask Server.py ausführen")
    print()
    while True:
        player_choice = input("Was wählst du? (schere, stein, papier, echse, spock): ").lower()
        # .name: https://realpython.com/python-enum/#using-the-name-and-value-attributes
        if player_choice not in [choice.name for choice in weapon]:
            print("ungültige Eingabe. Bitte gib wirklich das Wort so ein, so wie es da steht.")
            # https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
            continue
        computer_choice = get_computer_choice()
        player_choices.append(player_choice)
        computer_choices.append(computer_choice.name)
        winner = get_winner(weapon[player_choice], computer_choice)
        if winner == "noone":
            print("unentschieden!")
        elif winner == "computer":
            print("der Computer hat", computer_choice.name, "gewählt und gewinnt somit diese Runde!")
            computer_wins += 1
        elif winner == "player":
            print("Du hast", player_choice, "gewählt und gewinnst somit diese Runde!")
            print("    nur so nebenbei: der Computer hat ", computer_choice.name, "gewählt und somit verloren")
            player_wins += 1
        else:
            print("etwas ist mächtig schief gelaufen!!!!")

        print()
        print("Spiele gewonnen: ")
        print("Spieler: ", player_wins, "Computer: ", computer_wins)

        play_again = input("nochmal spielen ? (j / n) (beim Aussteigen wird eine Simple Statistik angezeigt): ")
        if not play_again or play_again.lower()[0] == "n":
            # https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
            break

    print("Danke fürs Spielen, bis zum nächsten mal!")
    print("Der Spieler hat in dieser Reihenfolge gewählt:")
    for choice in player_choices:
        print("-", choice)
    print("Der Computer hat in dieser Reihenfolge gewählt:")
    for choice in computer_choices:
        print("-", choice)

    print()


    # Wins speichern
    saveToDB("player", player_wins)
    saveToDB("computer", computer_wins)

    sum_wins_player = 0
    sum_wins_computer = 0

    dbDict = json.loads(getFromDB())
    for user in dbDict:
        if user['name'] == 'player':
            sum_wins_player = user['amount']
        elif user['name'] == 'computer':
            sum_wins_computer = user['amount']

    print("aus der Datenbank geladene Statistik:")
    print("gesamt gewonnene Spiele vom Spieler: ")
    print(sum_wins_player)
    print("gesamt gewonnene Spiele vom Computer: ")
    print(sum_wins_computer)


def saveToDB(name, amount):
    url = 'http://127.0.0.1:5000/updateTotalWins'
    data = {
        'name': name,
        'amount': amount
    }
    response = requests.post(url, data=data)
    print(response.text)


def getFromDB():
    url = 'http://127.0.0.1:5000/getTotalWins'
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    main()
