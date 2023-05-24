package Drucker_Proxy;

public class SWDrucker implements IDrucker{

    public void drucken(int Seiten) {
        System.out.printf("Es werden / wird %d Seite(n) in SW gedruckt...", Seiten);
    }

    public void drucken(int Seiten, DruckOptionen drucko) {
        this.drucken(Seiten);
    }
}
