public class Verifier3 {
    private static String encrypted = "obwaohfcbwq";
    public static boolean verifyFlag(String candidate) {
        if(candidate.length() != encrypted.length()){
            return false;
        }

        for(int i = 0; i < encrypted.length(); i++){
            if(!Character.isLowerCase(candidate.charAt(i))){
                return false;
            }
            
            if((encrypted.charAt(i) - 'a' + 12) % 26 != candidate.charAt(i) - 'a'){
                return false;
            }
        }

        return true;
    }
}
