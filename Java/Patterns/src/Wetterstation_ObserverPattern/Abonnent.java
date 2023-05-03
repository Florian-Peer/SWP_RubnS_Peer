package Wetterstation_ObserverPattern;

import java.util.Date;

public interface Abonnent {

    public void erhalteDaten(Daten daten);
}

  class Bildschirm implements Abonnent {


    @Override
    public void erhalteDaten(Daten daten) {
        System.out.println("Screendisplay: Temp: " + daten.getTemp() +" Humid: "+ daten.getHumid());
    }
    //*/

    //pull:
      /*
      @Override
      public void erhalteDaten(ServerPublisher serverPublisher){
          System.out.println("Screendisplay: Temp: " + serverPublisher.getAktuelleDaten().getTemp() +" Humid: "+ serverPublisher.getAktuelleDaten().getHumid());
      }
      //*/

}

 class Farbsignal implements Abonnent {

    @Override
    public void erhalteDaten(Daten daten) {
        System.out.print("Farbdisplay: ");
        if(daten.getTemp() < 5) {
            System.out.println("ROT");
        }
        else{
            System.out.println("GRÜN");
        }
    }
    //*/
//Pull
    /*
     @Override
     public void erhalteDaten(ServerPublisher serverPublisher) {
         System.out.println("Farbdisplay: ");
         if(serverPublisher.getAktuelleDaten().getTemp() < 5) {
             System.out.println("ROT");
         }
         else{
             System.out.println("GRÜN");
         }
     }
     //*/
}
