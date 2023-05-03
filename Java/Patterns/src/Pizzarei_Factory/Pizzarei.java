package Pizzarei_Factory;

public abstract class Pizzarei {
    public abstract String getBacken();
    public abstract int getSchneiden();
    public abstract String getEinpacken();

    @Override
    public String toString(){
        return "Zutaten = " + this.getBacken() + "   Anzahl Stücke = " + this.getSchneiden() + "   Verpackung = " + this.getEinpacken();
    }

}
