/*
 * Given two strings, write a method to decide if one is a permutation of the other.
 */

import java.util.Arrays;

public class CheckPermutation {

    public static char[] sortString(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return chars;
    }

	public static Boolean checkPermutation(String input1, String input2) {

        if (input1.length() != input2.length()) {
            return false;
        }

        return Arrays.equals(sortString(input1), sortString(input2));
	}

	public static void main(String[] args) {
        String s1 = "Buffalo";
        String s2 = "Bills";
        Boolean out1 = checkPermutation(s1, s2);
        // should print False
		System.out.println(out1);      

        String s3 = "dog";
        String s4 = "god";
        Boolean out2 = checkPermutation(s3, s4);        
        // should print True
		System.out.println(out2);
	}

}

/*
	Running from command line:
		1) javac *.java <--- compile java file to class file
		2) java * <--- Execute compiled Java file
*/