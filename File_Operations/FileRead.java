import java.io.*;

public class FileRead {

	public static String readFile(String input) {

		try {
			FileReader fr = new FileReader(input);
			BufferedReader in = new BufferedReader(fr);
			String output = "";
			String line = null;
			while((line = in.readLine()) != null) {
				output = output + line + "\n";
			}
			return output;
		}
		catch(IOException e) {
			System.out.println("Error occurred while trying to read " + input);
		}
		return "";
	}

	public static void main(String[] args) {
		String out = readFile("read.txt");
		System.out.println(out);
	}

}

/*
	Running from command line:
		1) javac FileRead.java <--- compile java file to class file
		2) java FileRead <--- Execute compiled Java file
*/