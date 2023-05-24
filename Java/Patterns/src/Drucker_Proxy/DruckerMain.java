package Drucker_Proxy;

public class DruckerMain {
    public static void main(String[] args) {
        DruckerProxy drucker = new DruckerProxy();

        try {
            drucker.drucken(10, DruckOptionen.farbe);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
