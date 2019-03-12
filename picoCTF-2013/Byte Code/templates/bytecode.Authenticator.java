import java.util.Scanner;
import java.io.*;

class Authenticator
{
	public static char[] key;
	public Authenticator(){}
	public static void main(String []args)
	{
		key = new char[10];
		key[0] = ###char0###;
		key[1] = ###char1###;
		key[2] = ###char2###;
		key[3] = ###char3###;
		key[4] = ###char4###;
		key[5] = ###char5###;
		key[6] = ###char6###;
		key[7] = ###char7###;
		key[8] = ###char8###;
		key[9] = ###char9###;
		Console console = System.console();
		String input = "";
		while(!input.equals("###string###"))
			input = console.readLine("Enter password:");
		for(int i=0; i<key.length; i++)
			System.out.print(key[i]);
		System.out.println("");
	}
}