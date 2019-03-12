
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TunnelGenerator {
    
    static class Password {
        String password = "";
        String hint = "";
        public Password() {
            for(int i = 0; i < 20; i++){
                double rand = Math.random();
                if(rand < 0.25) {
                    password += (char)('a' + (int)Math.floor(26 * Math.random()));
                }else if(rand < 0.5){
                    password += (char)('0' + (int)Math.floor(10 * Math.random()));
                }else if(rand < 0.75){
                    password += (Math.random() > 0.5? " ": "\t");
                }else{
                    password += (char)('A' + (int)Math.floor(26 * Math.random()));
                }
            }
            
            List<Integer> candidates = new ArrayList<>(password.length());
            for(int i = 0; i < password.length(); i++){
                candidates.add(i);
            }
            
            Collections.shuffle(candidates);
            
            List<Integer> toRemove = candidates.subList(0, 3);
            
            hint = "^";
            for(int i = 0; i < password.length(); i++) {
                if (toRemove.contains(i)) {
                    char hideChar = password.charAt(i);
                    String replacement = "";

                    if (Character.isLowerCase(hideChar)) {
                        replacement = "[a-z]";
                    } else if (Character.isUpperCase(hideChar)) {
                        replacement = "[A-Z]";
                    } else if (Character.isDigit(hideChar)) {
                        replacement = "\\d";
                    } else {
                        replacement = "\\s";
                    }
                    hint += replacement;
                } else {
                    hint += password.charAt(i);
                }
            }
            
            hint += "$";
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        
        Password pswd = new Password();
        String pass = pswd.password;
        String hint = pswd.hint;
        
        File flagFile = new File("flag.txt");
        PrintWriter pw = new PrintWriter(flagFile);
        pw.append("utflag{bean_pure_omission_production_rally}");
        pw.close();
        
        for(int i = 0; i < 1000; i++) {
            if(i == 0){
                Runtime.getRuntime().exec(new String[]{"/usr/bin/zip", "-P", pass, "newArchive.zip", "flag.txt"}).waitFor();
            }else {
                Runtime.getRuntime().exec(new String[]{"/usr/bin/zip", "-P", pass, "newArchive.zip", "hint.txt", "archive.zip"}).waitFor();
            }

            Runtime.getRuntime().exec(new String[]{"/bin/mv", "newArchive.zip", "archive.zip"}).waitFor();
            
            File hintFile = new File("hint.txt");
            pw = new PrintWriter(hintFile);
            pw.append(hint);
            pw.close();

            pswd = new Password();
            pass = pswd.password;
            hint = pswd.hint;
        }
    }
}
