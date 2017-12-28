/*
 * Implement a mtheod to perform baisc string compression using the counts of repeated characters. 
 * Ex: aabcccccaaa -> a2b1c5a3
 * If "compressed" string doesn't become smaller than the original string, return the original string.
 */

import java.util.Arrays;

public class StringCompression {

	public static String stringCompression(String s) {

        StringBuilder compressed = new StringBuilder();
        int consecutiveLetters = 0;
        for(int i = 0; i < s.length(); i++) {

            consecutiveLetters+=1;

            // check if the next letter is the same as the current letter or if we have reached the last letter in the string
            if (i+1 >= s.length() || s.charAt(i) != s.charAt(i+1)) {
                compressed.append(s.charAt(i));
                compressed.append(consecutiveLetters);
                consecutiveLetters = 0;
            }
        }

        return compressed.length() >= s.length() ? s : compressed.toString();
	}

	public static void main(String[] args) {
        String s1 = "aabcccccaaa";
        String s2 = "aaaaaaabb";
        String s3 = "abcde";

        String out1 = stringCompression(s1);
        String out2 = stringCompression(s2);
        String out3 = stringCompression(s3);

        System.out.println(out1); // prints a2b1c5a3
        System.out.println(out2); // a7b2
        System.out.println(out3); // abcde
	}
}

/*
	Running from command line:
		1) javac *.java <--- compile java file to class file
		2) java * <--- Execute compiled Java file
*/