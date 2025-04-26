import java.rmi.*;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelInterface hotel = (HotelInterface) Naming.lookup("rmi://localhost/HotelService");

            System.out.println(hotel.bookRoom("Ritika"));
            System.out.println(hotel.bookRoom("Shrawan"));
            System.out.println(hotel.bookRoom("Ritika")); // Duplicate booking
            System.out.println(hotel.cancelBooking("Shrawan"));
            System.out.println(hotel.cancelBooking("Karan")); // No booking

        } catch (Exception e) {
            System.out.println("Client Error: " + e.getMessage());
        }
    }
}
