public class Verifier2 {
    private static int[] encrypted = {3080674, 3110465, 3348793, 3408375, 3319002, 3229629, 3557330, 3229629, 3408375, 3378584};
    public static boolean verifyFlag(String candidate) {
        if(candidate.length() != encrypted.length){
            return false;
        }

        for(int i = 0; i < encrypted.length; i++){
            if(encrypted[i] != (candidate.substring(i, i+1) + "foo").hashCode()){
                return false;
            }
        }

        return true;
    }
}
