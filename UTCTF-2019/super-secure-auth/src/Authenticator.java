import java.util.StringTokenizer;

public class Authenticator {
    private static boolean checkFlag(String candidate) {
        try {
            if (!candidate.substring(0, 7).equals("utflag{")) {
                return false;
            }

            if (candidate.charAt(candidate.length() - 1) != '}') {
                return false;
            }

            StringTokenizer st = new StringTokenizer(candidate.substring(7, candidate.length() - 1), "_");

            if (!Verifier0.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier1.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier2.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier3.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier4.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier5.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier6.verifyFlag(st.nextToken())) {
                return false;
            }

            if (!Verifier7.verifyFlag(st.nextToken())) {
                return false;
            }

            return true;
        }catch(Exception e){
            return false;
        }
    }

    public static void main(String[] args) throws Exception{
        if(args.length != 1) {
            System.out.println("usage: java Authenticator [password]");
            return;
        }

        String candidate = args[0];

        if(checkFlag(candidate)){
            System.out.println("You got it! The flag is: " + candidate);
        }else{
            System.out.println("Oops, try again!");
        }
    }
}
