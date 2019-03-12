public class Verifier0 {
    private static byte[] encrypted = {50, 48, 45, 50, 42, 39, 54, 49};
    public static boolean verifyFlag(String candidate) {
        if(candidate.length() != encrypted.length){
            return false;
        }

        for(int i = 0; i < encrypted.length; i++){
            if(encrypted[i] != (candidate.charAt(i) ^ 0x42)){
                return false;
            }
        }

        return true;
    }
}
