import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Start registry programmatically (no need for separate `rmiregistry` command)
            LocateRegistry.createRegistry(5000);

            // Create and bind remote object
            ConcatImpl obj = new ConcatImpl();
            Naming.rebind("rmi://localhost:5000/concatService", obj);

            System.out.println("Server is running...");
        } catch (Exception e) {
            System.out.println("Server Exception: " + e);
        }
    }
}
