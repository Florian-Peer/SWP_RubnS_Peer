import random


class Knoten:
    def __init__(self, inhalt=None, naechster=None):
        self.inhalt = inhalt
        self.naechster = naechster

    def __str__(self):
        return str(self.inhalt)


class VerketteteListe:
    def __init__(self):
        self.laenge = 0
        self.kopf = None
        self.schwanz = None

    def anhaengen(self, inhalt):
        # erster Eintrag in der Liste is der Kopf
        neuer_knoten = Knoten(inhalt)
        if self.kopf is None:
            self.kopf = neuer_knoten
            self.schwanz = neuer_knoten
        else:
            self.schwanz.naechster = neuer_knoten
            # Aktualisiert den Schwanzzeiger auf den neuen Knoten
            self.schwanz = neuer_knoten
        self.laenge += 1

    def __iter__(self):
        zeiger = self.kopf
        while zeiger:
            # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
            # durch das yield benötigt man kein __next__ für den Iterator
            yield zeiger.inhalt
            zeiger = zeiger.naechster

    def __str__(self):
        # die Elemente der Liste schön ausgeben, mit Pfeil zum Veranschaulichen der Struktur
        elemente = []
        zeiger = self.kopf
        while zeiger:
            elemente.append(str(zeiger))
            zeiger = zeiger.naechster
        return " ==> ".join(elemente)


def main():
    # Knoten werden erzeugt, sind aber noch nicht verkettet
    knoten1 = Knoten(10)
    knoten2 = Knoten(20)
    knoten3 = Knoten(30)

    # hier werden die einzelnen Knoten verkettet
    knoten1.naechster = knoten2
    knoten2.naechster = knoten3
    """
    jetzt schauen die einzelnen Knoten so aus:

    knoten1                     knoten2                     knoten3
    inhalt = 10                 inhalt = 20                 inhalt = 30
    naechster = knoten2         naechster = knoten3         naechster = None (Ende der Liste)
    """

    # für das Erstellen der verketteten Liste muss kein Knoten erstellt werden; das wird in anhaengen erledigt
    liste = VerketteteListe()
    liste.anhaengen(100)
    for i in range(9):
        liste.anhaengen(random.randint(1, 100))

    print("Länge der Liste: ")
    print(liste.laenge)
    print("Inhalt in der Liste: ")
    print(liste)
    print()

    print("Elemente über Iterator:")
    for inhalt in liste:
        print(inhalt)


if __name__ == "__main__":
    main()
