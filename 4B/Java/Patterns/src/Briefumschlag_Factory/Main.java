package Briefumschlag_Factory;

public class Main {
    public static void main(String[] args) {
        EnvelopeFactory ev = new EnvelopeFactory();

        Envelope a4Envelope = ev.getEnvelope(Size.A4);
        Envelope a5Envelope = ev.getEnvelope(Size.A5);
        Envelope a6Envelope = ev.getEnvelope(Size.A6);

        System.out.println(a4Envelope);
        System.out.println(a5Envelope.getSize() + " " + a5Envelope.getWeight());
        System.out.println(a6Envelope.getSize() + " " + a6Envelope.getWeight());

    }
}
