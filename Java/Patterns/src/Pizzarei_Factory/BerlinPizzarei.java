package Pizzarei_Factory;

public class BerlinPizzarei extends Pizzarei {
    public String zutaten;
    public int anzahl;
    public String verpackung;

    public BerlinPizzarei(String art){
        if("Salami".equalsIgnoreCase(art)) {
            this.zutaten = "Salami";
            this.anzahl = 8;
            this.verpackung = "rot Karton";
        }
        else if("Calzone".equalsIgnoreCase(art)) {
            this.zutaten = "Schinken";
            this.anzahl = 8;
            this.verpackung = "gelb Karton";
        }
        else if("Hawaii".equalsIgnoreCase(art)) {
            this.zutaten = "Ananas, extra schinken";
            this.anzahl = 4;
            this.verpackung = "grün Karton";
        }

    }
    @Override
    public String getBacken(){
        return this.zutaten;
    }
    @Override
    public int getSchneiden(){
        return this.anzahl;
    }
    @Override
    public String getEinpacken(){
        return this.verpackung;
    }
}
