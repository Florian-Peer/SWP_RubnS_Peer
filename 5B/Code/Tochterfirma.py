class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        # muss in einer Abteilung sein
        self.abteilung = abteilung


class Abteilungsleiter(Mitarbeiter):
    # keine zusätzlichen Anforderungen zum regulären Mitarbeiter
    pass


# ------------------------------------------------------------------
class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def hinzufuegen_mitarbeiter(self, eingegebenerMitarbeiter):
        # wenn der Mitarbeiter ein Abteilungsleiter ist
        if isinstance(eingegebenerMitarbeiter, Abteilungsleiter):
            # und die Abteilungsleiterposition noch nicht belegt ist
            if not self.leiter:
                self.leiter = eingegebenerMitarbeiter
            else:
                raise ValueError("Es gibt bereits einen Abteilungsleiter in dieser Abteilung!")
        self.mitarbeiter.append(eingegebenerMitarbeiter)

    def mitarbeiteranzahl(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def abteilungHinzufügen(self, abteilung):
        self.abteilungen.append(abteilung)

    # wie viele Mitarbeiter, Abteilungsleiter gibts in der Firma
    def gesamt_mitarbeiteranzahl(self):
        return sum(abteilung.mitarbeiteranzahl() for abteilung in self.abteilungen)

    def abteilungsleiter_anzahl(self):
        return sum(1 for abteilung in self.abteilungen if abteilung.leiter is not None)

    # wie viel Abteilungen gibt es
    def abteilungsanzahl(self):
        return len(self.abteilungen)

    # welche Abteilung hat die größte Mitarbeiterstärke (am meisten Mitarbeiter)
    def abteilung_mit_meisten_mitarbeitern(self):
        max_mitarbeiteranzahl = 0
        abteilung_mit_max_mitarbeiter = None

        for abteilung in self.abteilungen:
            if abteilung.mitarbeiteranzahl() > max_mitarbeiteranzahl:
                max_mitarbeiteranzahl = abteilung.mitarbeiteranzahl()
                abteilung_mit_max_mitarbeiter = abteilung

        return abteilung_mit_max_mitarbeiter

    def geschlechterverteilung(self):
        maenner = 0
        frauen = 0
        for abteilung in self.abteilungen:
            for arbeiter in abteilung.mitarbeiter:
                if arbeiter.geschlecht.lower() == 'männlich':
                    maenner += 1
                elif arbeiter.geschlecht.lower() == 'weiblich':
                    frauen += 1
        total = maenner + frauen
        if total > 0:
            return {"männlich": maenner / total * 100, "weiblich": frauen / total * 100}
        return {"männlich": 0, "weiblich": 0}


def main():
    meine_firma = Firma("Flosengemüse")

    abteilung1 = Abteilung("Entwicklung")
    abteilung2 = Abteilung("Vertrieb")

    meine_firma.abteilungHinzufügen(abteilung1)
    meine_firma.abteilungHinzufügen(abteilung2)

    mitarbeiter1 = Mitarbeiter("Brunhilde", "weiblich", abteilung1)
    mitarbeiter1_2 = Mitarbeiter("Herta", "weiblich", abteilung1)
    leiter1 = Abteilungsleiter("Bruno", "männlich", abteilung1)
    leiter1_2 = Abteilungsleiter("Leopold", "männlich", abteilung1)
    mitarbeiter2 = Mitarbeiter("Klaus", "männlich", abteilung2)
    mitarbeiter2_2 = Mitarbeiter("Eberhart", "männlich", abteilung2)

    abteilung1.hinzufuegen_mitarbeiter(mitarbeiter1)
    abteilung1.hinzufuegen_mitarbeiter(mitarbeiter1_2)
    abteilung1.hinzufuegen_mitarbeiter(leiter1)
    abteilung2.hinzufuegen_mitarbeiter(mitarbeiter2)
    abteilung2.hinzufuegen_mitarbeiter(mitarbeiter2_2)

    print("Gesamtanzahl der Mitarbeiter:", meine_firma.gesamt_mitarbeiteranzahl())
    print("Anzahl der Abteilungsleiter:", meine_firma.abteilungsleiter_anzahl())
    print("Anzahl der Abteilungen:", meine_firma.abteilungsanzahl())
    print("Abteilung mit den meisten Mitarbeitern:", meine_firma.abteilung_mit_meisten_mitarbeitern().name)
    print("Geschlechterverteilung:", meine_firma.geschlechterverteilung())


if __name__ == "__main__":
    main()
