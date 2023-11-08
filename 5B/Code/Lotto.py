import random
import matplotlib.pyplot as plt


def ziehe_lottozahlen():
    ziehung = []
    while len(ziehung) < 6:
        zufallszahl = random.randint(1, anzahlZahlen)
        if zufallszahl not in ziehung:
            ziehung.append(zufallszahl)
    print("Zahlen in dieser Ziehung: ")
    print(ziehung)
    return ziehung


def lotto_statistik(anzahl_ziehungen):
    statistik = {}
    for i in range(anzahl_ziehungen):
        ziehung = ziehe_lottozahlen()
        for zahl in ziehung:
            if zahl in statistik:
                statistik[zahl] += 1
            else:
                statistik[zahl] = 1
    return statistik


# Parameter zum Einstellen

anzahlZahlen = 45
anzahlZiehungen = 1000

statistik = lotto_statistik(anzahlZiehungen)


# Statistik als Diagramm darstellen
plt.bar(statistik.keys(), statistik.values())
plt.xlabel('Zahl')
plt.ylabel('Häufigkeit der Zahl')
plt.title('Lottoziehung Statistik')
plt.show()
