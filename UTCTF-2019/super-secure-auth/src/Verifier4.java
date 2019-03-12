public class Verifier4 {
    private static int[] encrypted = {3376, 3295, 3646, 3187, 3484, 3268};
    public static boolean verifyFlag(String candidate) {
        if(candidate.length() != encrypted.length){
            return false;
        }

        for(int i = 0; i < encrypted.length; i++){
            if(encrypted[i] != (candidate.charAt(i) * 27 + 568)){
                return false;
            }
        }

        return true;
    }
}
