public class Drucker {

        public static void main(String[] args) {
            Drucker d1 = Drucker.getInstance();
            Drucker d2 = Drucker.getInstance();

            if (d1 == d2) {
                System.out.println("es gibt nur eine Instanz");
            } else {
                System.out.println("es existieren mehrere Instanzen");
            }

        }

    private static Drucker instance = null;
    private String drucker;

    private Drucker() {
        System.out.println("ich drucke, bin die Instanz XYZ");
    }

    public static synchronized Drucker getInstance() {
        if (instance == null) {
            instance = new Drucker();
        }
        return instance;
    }

    public String getDrucker() {
        return drucker;
    }
}
