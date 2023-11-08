package Briefumschlag_Factory;

public class A6_Envelope implements Envelope {
    private static Size SIZE = Size.A6;
    private static double WEIGHT = 6.0;

    @Override
    public Size getSize() {
        return SIZE;
    }

    @Override
    public double getWeight() {
        return WEIGHT;
    }
}
