package Pizzarei_Factory;

public class HamburgPizzarei extends Pizzarei {
    public String zutaten;
    public int anzahl;
    public String verpackung;
    public HamburgPizzarei(String art){
        if("Salami".equalsIgnoreCase(art)) {
            this.zutaten = "Salami, Pfefferoni";
            this.anzahl = 8;
            this.verpackung = "grün Karton";
        }
        else if("Calzone".equalsIgnoreCase(art)) {
            this.zutaten = "Prosciutto";
            this.anzahl = 4;
            this.verpackung = "gelb Karton";
        }
        else if("Hawaii".equalsIgnoreCase(art)) {
            this.zutaten = "Ananas, keine Tomatensoße";
            this.anzahl = 2;
            this.verpackung = "rot Karton";
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
