public class BinarySearch {

	public static int binarySearch(int[] sortedArray, int value) {
		int low = sortedArray[0];
		int high = sortedArray[sortedArray.length - 1];
		while(low <= high){
			int mid = (low+high) / 2;
			if(mid > value){
				high = mid - 1;
			}
			else if(mid < value){
				low = mid + 1;
			}
			else {
				return mid;
			}
		}
		return -1;	
	}

	public static void main(String[] args) {
		int[] sortedArray = {0,1,2,3,4,5,6,7,8,9};
		int value = 7;
		System.out.println("Goal: " + value);
        System.out.println("Iterative Binary Search");
        System.out.println("Index: " + binarySearch(sortedArray, value));
        
        value = 11;
		System.out.println("Goal: " + value);
        System.out.println("Iterative Binary Search");
        System.out.println("Index: " + binarySearch(sortedArray, value));
	}

}

/*
	Running from command line:
		1) javac BinarySearch.java <--- compile java file to class file
		2) java BinarySearch <--- Execute compiled Java file
*/