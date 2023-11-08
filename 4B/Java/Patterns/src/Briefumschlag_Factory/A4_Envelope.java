package Briefumschlag_Factory;

public class A4_Envelope implements Envelope {

    private static Size size = Size.A4;
    private static double weight=10.0;

    @Override
    public Size getSize() {
        return size;
    }

    @Override
    public double getWeight() {
        return weight;
    }

    @Override
    public String toString(){
        return A4_Envelope.size + " " + A4_Envelope.weight;
    }
}
