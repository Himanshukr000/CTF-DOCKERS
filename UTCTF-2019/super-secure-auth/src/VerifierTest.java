public class VerifierTest {
    public static void main(String[] args) {//flag: utflag{prophets_anxious_demolition_animatronic_herald_fizz_stop_goodbye}
        Verifier0 v0 = new Verifier0();
        System.out.println(v0.verifyFlag("prophets"));
        
        Verifier1 v1 = new Verifier1();
        System.out.println(v1.verifyFlag("anxious"));
        
        Verifier2 v2 = new Verifier2();
        System.out.println(v2.verifyFlag("demolition"));
        
        Verifier3 v3 = new Verifier3();
        System.out.println(v3.verifyFlag("animatronic"));

        Verifier4 v4 = new Verifier4();
        System.out.println(v4.verifyFlag("herald"));
        
        Verifier5 v5 = new Verifier5();
        System.out.println(v5.verifyFlag("fizz"));
        
        Verifier6 v6 = new Verifier6();
        System.out.println(v6.verifyFlag("stop"));
        
        Verifier7 v7 = new Verifier7();
        System.out.println(v7.verifyFlag("goodbye"));
    }
}
