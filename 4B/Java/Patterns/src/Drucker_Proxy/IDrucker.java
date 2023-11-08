package Drucker_Proxy;

public interface IDrucker {
    void drucken(int druckInt) throws Exception;
    void drucken(int druckInt, DruckOptionen drucko) throws Exception;
}
