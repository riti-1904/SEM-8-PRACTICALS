import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class ConcatImpl extends UnicastRemoteObject implements ConcatInterface {
    public ConcatImpl() throws RemoteException {
        super();
    }

    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}
