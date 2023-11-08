package Wetterstation_ObserverPattern;
import java.util.*;

public class ServerPublisher {

    private List<Abonnent> abonnentlist = new ArrayList<Abonnent>();
    private Daten aktuelleDaten;

    public void aboHinzufuegen(Abonnent abonnent) {
        abonnentlist.add(abonnent);
    }

    public void aboEntfernen(Abonnent abonnent) {
        abonnentlist.remove(abonnent);
    }

    private void verteileDaten(Daten daten) {
        for (Abonnent abonnent : abonnentlist) {
            abonnent.erhalteDaten(daten);
        }
    }

    public void setAktuelleDaten(Daten aktuelleDaten) {
        this.aktuelleDaten = aktuelleDaten;
        verteileDaten(aktuelleDaten);
    }

    public Daten getAktuelleDaten() {
        return aktuelleDaten;
    }
}
