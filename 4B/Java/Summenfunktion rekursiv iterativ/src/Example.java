public class Example {
    public static double preisBerechnung(int item,double rohpreis, int multiplikator){
        return rohpreis*multiplikator;
    }
    public static double preiselbeerBerechnen(){
        return preisBerechnung(998,1,5);


    }
    public static double joguhrtBerechnen(){
        return preisBerechnung(999,9,2);

    }

    public static void main(String[] args) {
        double preis2 = preiselbeerBerechnen();
        double preis3 = joguhrtBerechnen();
    }
}
