package Drucker_Proxy;

public class DruckerProxy implements IDrucker {
    private IDrucker _drucker;
    private final int farbSeitenMaximal = 50;
    private final int seitenMaximal = 500;

    public DruckerProxy() {
    }

    public void drucken(int druckInt) throws Exception {
        if (druckInt <= 0) {
            throw new Exception("weniger als eine Seite drucken ist schlecht möglich und echt dumm von dir.\nBitte Seitenzahl erhöhen");
        } else if (druckInt > seitenMaximal) {
            throw new Exception("dein Drucker schafft keine 500 Seiten!! \nbitte weniger als 500 Seiten drucken");
        } else {
            if (druckInt < farbSeitenMaximal) {
                this._drucker = new FarbDrucker();
            } else {
                this._drucker = new SWDrucker();
            }

            this._drucker.drucken(druckInt);
        }
    }

    public void drucken(int druckInt, DruckOptionen drucko) throws Exception {
        if (druckInt <= 0) {
            throw new Exception("weniger als eine Seite drucken ist schlecht möglich und echt dumm von dir. \nBitte Seitenzahl erhöhen");
        } else if (druckInt > seitenMaximal) {
            throw new Exception("dein Drucker schafft keine 500 Seiten!! \nbitte weniger als 500 Seiten drucken");
        } else {
            if (drucko == DruckOptionen.farbe && druckInt < farbSeitenMaximal) {
                this._drucker = new FarbDrucker();
            } else {
                this._drucker = new SWDrucker();
            }

            this._drucker.drucken(druckInt);
        }
    }
}
