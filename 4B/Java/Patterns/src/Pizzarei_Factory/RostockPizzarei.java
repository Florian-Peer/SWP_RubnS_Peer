package Pizzarei_Factory;

public class RostockPizzarei extends Pizzarei {
    public String zutaten;
    public int stück;
    public String verpackung;
    public RostockPizzarei(String art){
        if("Salami".equalsIgnoreCase(art)) {
            this.zutaten = "Salami, Käserand";
            this.stück = 4;
            this.verpackung = "gelber Karton";
        }
        else if("Calzone".equalsIgnoreCase(art)) {
            this.zutaten = "Schinken, Pilze";
            this.stück = 1;
            this.verpackung = "rot Karton";
        }
        else if("Hawaii".equalsIgnoreCase(art)) {
            this.zutaten = "Ananas, Datteln";
            this.stück = 2;
            this.verpackung = "grün Karton";
        }

    }
    @Override
    public String getBacken(){
        return this.zutaten;
    }
    @Override
    public int getSchneiden(){
        return this.stück;
    }
    @Override
    public String getEinpacken(){
        return this.verpackung;
    }
}
