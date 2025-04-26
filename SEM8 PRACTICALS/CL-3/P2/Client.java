import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            ConcatInterface stub = (ConcatInterface) Naming.lookup("rmi://localhost:5000/concatService");
            String result = stub.concatenate("Hello, ", "World!");
            System.out.println("Concatenated String: " + result);
        } catch (Exception e) {
            System.out.println("Client Exception: " + e);
        }
    }
}
