public class BinarySearch {

	// iterative binary search
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

	// recursive binary search
	public static int binarySearch(int[] sortedArray, int value, int low, int high) {
		int mid = (low + high) / 2;
		if(low > high) {
			return -1;
		}
		if(sortedArray[mid] > value) {
			return binarySearch(sortedArray, value, low, mid-1);
		}
		else if(sortedArray[mid] < value) {
			return binarySearch(sortedArray, value, mid+1, high);
		}
		else {
			return mid;
		}
	}

	public static void main(String[] args) {
		int[] sortedArray = {0,1,2,3,4,5,6,7,8,9};
		int value = 7;
		System.out.println("Iterative Binary Search");
		System.out.println("-----------------------");
		System.out.println("Goal: " + value);	
		System.out.println("Index: " + binarySearch(sortedArray, value));
		value = 11;
		System.out.println("Goal: " + value);
		System.out.println("Index: " + binarySearch(sortedArray, value));

		System.out.println("=======================");
		
		System.out.println("Recursive Binary Search");
		System.out.println("-----------------------");
		int low = 0;
		int high = sortedArray.length - 1;
		value = 4;
		System.out.println("Goal: " + value);		
		System.out.println("Index: " + binarySearch(sortedArray, value, low, high));
		value = 20;
		System.out.println("Goal: " + value);
		System.out.println("Index: " + binarySearch(sortedArray, value, low, high));
	}

}

/*
	Running from command line:
		1) javac BinarySearch.java <--- compile java file to class file
		2) java BinarySearch <--- Execute compiled Java file
*/