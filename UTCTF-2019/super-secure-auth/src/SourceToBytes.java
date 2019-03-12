import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.util.Arrays;

public class SourceToBytes {
    static byte[] toBytes(String code, String className) throws IOException, InterruptedException {
        PrintWriter fout = new PrintWriter(className + ".java");
        
        fout.write(code);
        
        fout.close();
        
        new ProcessBuilder("/usr/bin/javac", className + ".java").inheritIO().start().waitFor();
        
        return Files.readAllBytes(new File(className + ".class").toPath());
    }
    
    public static void main(String[] args) throws IOException, InterruptedException {
        String testSource = "public class Verifier0 {\n" +
                "    private static byte[] encrypted = {23,22,4,46,35,37,57,11,29,42,114,50,39,29,55,29,38,115,38,44,54,29,38,114,29,54,42,35,54,29,32,59,29,42,3,44,38,63};\n" +
                "    public static boolean verifyFlag(String candidate) {\n" +
                "        if(candidate.length() != encrypted.length){\n" +
                "            return false;\n" +
                "        }\n" +
                "\n" +
                "        for(int i = 0; i < encrypted.length; i++){\n" +
                "            if(encrypted[i] != (candidate.charAt(i) ^ 0x42)){\n" +
                "                return false;\n" +
                "            }\n" +
                "        }\n" +
                "\n" +
                "        return true;\n" +
                "    }\n" +
                "}\n";
        
        System.out.println(Arrays.toString(toBytes(testSource, "Verifier0")));
    }
}
