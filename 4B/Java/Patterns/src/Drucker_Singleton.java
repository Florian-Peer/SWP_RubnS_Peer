public class Drucker_Singleton {

        public static void main(String[] args) {
            Drucker_Singleton d1 = Drucker_Singleton.getInstance();
            Drucker_Singleton d2 = Drucker_Singleton.getInstance();

            if (d1 == d2) {
                System.out.println("es gibt nur eine Instanz");
            } else {
                System.out.println("es existieren mehrere Instanzen");
            }

        }

    private static Drucker_Singleton instance = null;
    private String drucker;

    private Drucker_Singleton() {
        System.out.println("ich drucke, bin die Instanz XYZ");
    }

    public static synchronized Drucker_Singleton getInstance() {
        if (instance == null) {
            instance = new Drucker_Singleton();
        }
        return instance;
    }

    public String getDrucker() {
        return drucker;
    }
}
