package Briefumschlag_Factory;

public class A5_Envelope implements Envelope {
    private static Size SIZE = Size.A5;
    private static double WEIGHT = 8.0;

    @Override
    public Size getSize() {
        return SIZE;
    }

    @Override
    public double getWeight() {
        return WEIGHT;
    }
}
