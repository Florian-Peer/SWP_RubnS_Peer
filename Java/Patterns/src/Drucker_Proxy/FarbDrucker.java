package Drucker_Proxy;

public class FarbDrucker implements IDrucker {

    public void drucken(int Seiten) {
        System.out.printf("Es werden / wird %d Seite(n) in Farbe gedruckt...", Seiten);
    }

    public void drucken(int Seiten, DruckOptionen drucko) {
        this.drucken(Seiten);
    }
}
