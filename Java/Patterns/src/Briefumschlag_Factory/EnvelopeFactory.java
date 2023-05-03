package Briefumschlag_Factory;

public class EnvelopeFactory {
    public static Envelope getEnvelope(Size size) {
        if (size.equals(Size.notDefined)) {
            return null;
        }

        if (size.equals(Size.A4)) {
            return new A4_Envelope();
        } else if (size.equals(Size.A5)) {
            return new A5_Envelope();
        } else if (size.equals(Size.A6)) {
            return new A6_Envelope();
        }

        return null;
    }
}
