package Pizzarei_Factory;

public class PizzaFactory {
    public static Pizzarei getPizza(String stadt, String art){
        if("Berlin".equalsIgnoreCase(stadt)){
            return new BerlinPizzarei(art);
        }else if("Rostock".equalsIgnoreCase(stadt)){
            return new RostockPizzarei(art);
        }else if("Hamburg".equalsIgnoreCase(stadt)){
            return new HamburgPizzarei(art);
        }
        return null;
    }
}
