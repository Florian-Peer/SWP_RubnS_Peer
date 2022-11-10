public class FakEndrekursion {
    public static int Recursion(int n) {
        if (n <= 0) {
            return -1;
        } else {
            return End(1, n);
        }
    }

    //Wrapper Methode
    public static int EndRecursion(int n) {

            return End(1, n);

    }

    public static int End(int m, int n) {
        // wozu? Im schneller voran zu kommen
        // Ist ein Zwischenschritt zur Interation
        //vieles wird in der Variable m gespeichert
        if (n == 0) {

            //letzter Methodenaufruf
            return m;
        } else {
            System.out.println(m + " * " + n);
            return End(m * n, n - 1);
        }

    }

    public static void main(String[] args) {

        int n =6;
        int result = Recursion(n);

        //int result2 = End(1,n);
        int result3 = EndRecursion(n);

        if (result == -1) {
            System.out.println("Eingabe zu niedrig");
        } else {

            System.out.println("Ergebnis = " + result);
        }


    }
}









