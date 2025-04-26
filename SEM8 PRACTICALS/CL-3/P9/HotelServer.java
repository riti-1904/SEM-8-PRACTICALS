import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;
import java.util.*;

public class HotelServer extends UnicastRemoteObject implements HotelInterface {
    private HashMap<String, String> bookings;

    public HotelServer() throws RemoteException {
        bookings = new HashMap<>();
    }

    public String bookRoom(String guestName) throws RemoteException {
        if (!bookings.containsKey(guestName)) {
            bookings.put(guestName, "Booked");
            return "Room booked for " + guestName;
        } else {
            return "Guest " + guestName + " already has a booking.";
        }
    }

    public String cancelBooking(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            bookings.remove(guestName);
            return "Booking cancelled for " + guestName;
        } else {
            return "No booking found for " + guestName;
        }
    }

    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099); // Start RMI registry programmatically
            HotelServer server = new HotelServer();
            Naming.rebind("HotelService", server);
            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            System.out.println("Server Error: " + e.getMessage());
        }
    }
}
