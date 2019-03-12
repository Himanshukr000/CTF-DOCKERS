
import javax.xml.bind.DatatypeConverter;
import java.security.MessageDigest;

public class Verifier6 {
    private static String hash = "1B480158E1F30E0B6CEE7813E9ECF094BD6B3745";

    public static boolean verifyFlag(String candidate) {
        
        if(candidate.length() != 4) return false;
        
        try{
            MessageDigest md = MessageDigest.getInstance("SHA1");
            
            md.update(candidate.getBytes());

            String candidateHash = DatatypeConverter.printHexBinary(md.digest());
            
            return candidateHash.equals(hash);
            
        }catch(Exception e) {
            return false;
        }
    }
}
