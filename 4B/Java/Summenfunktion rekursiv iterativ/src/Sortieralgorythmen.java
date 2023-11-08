public class Sortieralgorythmen {

    public static int[] unsorted = {10,5,9,2,8,3,7,4,6,1};

    public static void main(String[] args) {
        unsorted = myInsertionSort(unsorted);

        for(int  element : unsorted){
            System.out.println(element);
        }
    }



    public static int[] myBubblesort(int[] elements){
        for(int max = elements.length -1; max > 0; max--){
            for(int i = 0; i<max; i++){
                if(elements[i] > elements[i+1]){
                    int temp= elements[i];
                    elements[i] = elements[i+1];
                    elements[i+1] = temp;
                }
            }
        }
        return elements;
    }

    public static int[] myInsertionSort(int[] elements) {
        for(int i = 1; i<elements.length; i++){
            int j = i;
            while (j>0 && elements[j] < elements[j-1]){
                int temp = elements[j];
                elements[j] = elements[j-1];
                elements[j-1] = temp;
                j--;
            }
        }
        return elements;
    }

    public static int[] mySelectionSort(int[] elements){
        for(int i =0; i<elements.length -1; i++){
            int minPos = i;
            for(int j = i+1; j<elements.length; j++){
                if(elements[j] < elements[minPos]){
                    minPos = j;
                }
            }
            if(minPos!=i){
                int temp = elements[i];
                elements[i] = elements[minPos];
                elements[minPos] = temp;
            }
        }
        return elements;
    }



}
