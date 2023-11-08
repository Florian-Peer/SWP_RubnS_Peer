package Wetterstation_ObserverPattern;

public class Daten {
    private  int temp;
    private  int humid;

    public Daten(int temp, int humid) {
        this.temp = temp;
        this.humid = humid;
    }

    public int getTemp() {
        return this.temp;
    }
    public int getHumid() {
        return this.humid;
    }

    public void setMeasurements(int temp, int humid){
        this.temp=temp;
        this.humid=humid;
    }


}
