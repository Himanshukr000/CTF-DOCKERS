import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class TunnelGenerator {
    private static final int LEVELS = 30;
    
    static String BytesToSource(byte[] arr, String className){
        StringBuilder sb = new StringBuilder("import java.util.Base64;\n" +
                "import java.util.BitSet;\n" +
                "public class " + className + " extends ClassLoader{\n" +
                "    private static byte[] arr = jBaseZ85.decode(");
        
        String encoded = new String(jBaseZ85.encode(arr));
        
        int numChunks = (encoded.length() + 10000 - 1) / 10000;
        
        for(int i = 0; i < numChunks; i++){
            sb.append("new String(\"" + encoded.substring(i * 10000, Math.min((i+1) * 10000, encoded.length())).replace("\\", "\\\\").replace("\"", "\\\""));
            sb.append("\")");
            
            if(i != numChunks - 1) {
                sb.append("+");
            }
        }
        
        sb.append(");\n" +
                "    public static boolean verifyFlag(String candidate) throws Exception {\n" +
                "        " + className + " l = new " + className+ "();\n" +
                "\n" + 
                "        Class verifier = l.defineClass(\"" + className + "\", arr, 0, arr.length);\n" +
                "\n" +
                "        Object a = verifier.getMethod(\"verifyFlag\", String.class).invoke(null, candidate);\n" +
                "        \n" +
                "        return (boolean)a;\n" +
                "    }\n" +
                "}\n");
        
        return sb.toString();
    }
    
    public static void main(String[] args) throws IOException, InterruptedException {
        
        for(int vnum = 0; vnum < 8; vnum++) {
            String currentSource = new Scanner(new File("src/Verifier" + vnum + ".java")).useDelimiter("\\Z").next();

            byte[] bytes = new byte[0];
            for (int i = 0; i < LEVELS; i++) {
                bytes = SourceToBytes.toBytes(currentSource, "Verifier" + vnum);
                currentSource = BytesToSource(bytes, "Verifier" + vnum);
                System.out.println(i);
            }
        }
    }
}
