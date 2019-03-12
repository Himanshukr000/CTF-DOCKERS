public class Verifier1 {
    private static byte[] encrypted = {115, 117, 111, 105, 120, 110, 97};
    public static boolean verifyFlag(String candidate) {
        if(candidate.length() != encrypted.length){
            return false;
        }

        for(int i = 0; i < encrypted.length; i++){
            if(encrypted[i] != candidate.charAt(encrypted.length - 1 - i)){
                return false;
            }
        }

        return true;
    }
}
