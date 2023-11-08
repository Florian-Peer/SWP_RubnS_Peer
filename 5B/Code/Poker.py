import random


def erstelle_hand():
    deck = list(range(1, 53))  # Erstellt ein Deck mit 52 Karten
    hand = random.sample(deck, 5)  # Zieht zufällig 5 Karten aus dem Deck
    return hand


def alle_gleiche_farbe(farben):
    erste_farbe = farben[0]
    for farbe in farben:
        if farbe != erste_farbe:
            return False
    return True


def bewerte_hand(hand):
    farben = [karte // 13 for karte in hand]
    kartenart = [karte % 13 for karte in hand]
    kartenart.sort()

    if alle_gleiche_farbe(farben) and kartenart == [0, 9, 10, 11, 12]:
        return "Royal Flush"
    if alle_gleiche_farbe(farben) and all(kartenart[i] == kartenart[i + 1] - 1 for i in range(4)):
        return "Straight Flush"
    if max(kartenart.count(k) for k in kartenart) == 4:
        return "Vierling"
    if len([k for k in kartenart if kartenart.count(k) == 2]) == 2 and len(
            [k for k in kartenart if kartenart.count(k) == 3]) == 3:
        return "Full House"
    if alle_gleiche_farbe(farben):
        return "Flush"
    if all(kartenart[i] == kartenart[i + 1] - 1 for i in range(4)):
        return "Straight"
    if max(kartenart.count(k) for k in kartenart) == 3:
        return "Drilling"
    if len([k for k in kartenart if kartenart.count(k) == 2]) == 4:
        return "Zwei Paare"
    if max(kartenart.count(k) for k in kartenart) == 2:
        return "Ein Paar"
    return "Hochkarte"


anzahl_runden = 500000
handbewertung_zähler = {
    "Hochkarte": 0,
    "Ein Paar": 0,
    "Zwei Paare": 0,
    "Drilling": 0,
    "Straight": 0,
    "Flush": 0,
    "Full House": 0,
    "Vierling": 0,
    "Straight Flush": 0,
    "Royal Flush": 0
}

for _ in range(anzahl_runden):
    spielerhand = erstelle_hand()
    handbewertung = bewerte_hand(spielerhand)
    handbewertung_zähler[handbewertung] += 1

gesamt_hände = anzahl_runden
for bewertung, anzahl in handbewertung_zähler.items():
    prozent = (anzahl / gesamt_hände) * 100
    print(f"{bewertung}: {prozent:.5f}%")
