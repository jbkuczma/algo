public class QuickSort {
    
    public void quickSort(int[] input, int low, int high) {
        if (low < high) {
            // index found from partition
            int pivot = partition(input, low, high);

            quickSort(input, low, pivot - 1);
            quickSort(input, pivot + 1, high);
        }
    }

    public int partition(int[] input, int low, int high) {
        int pivot = input[high];
        int left = low - 1;

        for (int i = low; i < high; i++) {
            if (input[i] <= pivot) {
                left+=1;

                // swap
                int temp = input[left];
                input[left] = input[i];
                input[i] = temp;
            }
        }

        int temp = input[left+1];
        input[left+1] = input[high];
        input[high] = temp;

        return left + 1;
    }

    public static void main(String[] args) {
        int numbers[] = {22, 4, 16, 891, 506, 2424, 88, 1, 99999, 345, 341, 6792, 8};

        System.out.println("Unsorted");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println("");        

        QuickSort qs = new QuickSort();
        qs.quickSort(numbers, 0, numbers.length-1);

        System.out.println("Sorted");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
    }

}
    
/*
    Running from command line:
        1) javac *.java <--- compile java file to class file
        2) java * <--- Execute compiled Java file
*/