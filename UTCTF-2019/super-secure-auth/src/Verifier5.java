import javax.xml.bind.DatatypeConverter;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Verifier5 {
    private static String encrypted = "8FA14CDD754F91CC6554C9E71929CCE7865C0C0B4AB0E063E5CAA3387C1A8741FBADE9E36A3F36D3D676C1B808451DD7FBADE9E36A3F36D3D676C1B808451DD7";
    public static boolean verifyFlag(String candidate) {
        try{
            MessageDigest md = MessageDigest.getInstance("MD5");

            String result = "";

            for(char c : candidate.toCharArray()) {
                md.update((byte)c);

                result += DatatypeConverter.printHexBinary(md.digest());
            }
            
            return result.equals(encrypted);
            
        }catch(Exception e) {
            return false;
        }
    }
}
