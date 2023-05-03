package Wetterstation_ObserverPattern;

/*
Modellieren Sie eine Wetterstation mittels Observer Pattern.

Eine Zentrale misst Temperatur und Luftfeuchtigkeit.
Diverse Anzeigen geben die Messwerte mittels Bilschirm oder Farbsignalen aus.
Überlegen Sie wie man PUSH und PULL Variante implementiert werden würde. (Also zwei Lösungen)

Programiere in Java, mache zustätzlich nicht optional ein UML Diagramm dazu!
 */

import java.util.Random;

public class WetterMain {
    public static void main(String[] args) {
        ServerPublisher server_P = new ServerPublisher();
        server_P.aboHinzufuegen(new Bildschirm());
        server_P.aboHinzufuegen(new Farbsignal());

        Random rand = new Random();
        /*
        int randomTemp = rand.nextInt((23 - 5) + 1) + 5;
        int randomHumid = rand.nextInt(61) + 30;
        */

        int randomTemp = rand.nextInt(-20, 40);
        int randomHumid = rand.nextInt(20, 100);


        server_P.setAktuelleDaten(new Daten(randomTemp, randomHumid));

    }
}
