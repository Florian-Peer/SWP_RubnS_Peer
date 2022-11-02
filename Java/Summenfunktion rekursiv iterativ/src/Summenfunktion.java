import java.io.Reader;
import java.util.Locale;
import java.util.Scanner;

public class Summenfunktion {
    static Scanner reader = new Scanner(System.in);
    public static void main(String[] args) {
        int zahl = 0;
        char wahl = ' ';

        System.out.println("Summenfunktion");
        System.out.println("Zahl eingeben: ");
        zahl = reader.nextInt();
        System.out.println("wie wollen Sie die Summenfunktion berechnen?\n");
        System.out.println("rekursiv ... r\niterativ ... i");
        wahl = reader.next().toLowerCase().charAt(0);

        if(wahl == 'r'){
            System.out.println("Wahl: rekursiv");
            System.out.println("Ergebnis: " + rekursiv(zahl));

        }
        else if(wahl == 'i'){
            System.out.println("Wahl: iterativ");
            System.out.println("Ergebnis: " + iterativ(zahl));
        }
        else {
            System.out.println("Falsche Eingabe!!");
        }
    }

    static int rekursiv(int n){
        System.out.println("Aufruf mit " + n);
        if(n>=1){
            return n + rekursiv(n-1);
        }
        else {
            return n;
        }
    }

    static int iterativ(int n){
        int ergebnis = 0;


        for(int i = 0; i<= n; i++){
            System.out.println("Aufruf mit " + (n-i));
            ergebnis+=i;
        }
        return ergebnis;
    }

}
