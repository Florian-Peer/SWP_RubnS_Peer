import java.util.Scanner;

public class Fakultät_rekursiv {
    static Scanner reader = new Scanner(System.in);
    public static void main(String[] args) {
        int zahl = 0;



        System.out.println("Zahl eingeben: ");
        zahl = reader.nextInt();



            System.out.println("Ergebnis: " + rekursiv(zahl));


    }

    static int rekursiv(int n){
        System.out.println("Aufruf mit " + n);
        if(n>=1){
            return n * rekursiv(n-1);
        }
        else {
            return 1;
        }
    }

}
