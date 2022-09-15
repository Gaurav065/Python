
import java.io.*;
import java.util.*;
 
class pg2{
 
    // Function to find the missing number
    public static void find_small_large_number(int arr[])
    {
        int smallest = arr[0];
        int largest = arr[0];
 
        for(int i=1; i< arr.length; i++){
            if(arr[i] > largest)
            largest = arr[i];
            else if (arr[i] < smallest)
            smallest = arr[i];
 
        }
    System.out.println("Smallest Number is : " + smallest);
    System.out.println("Largest Number is : " + largest);
    }
    // Driver Code
    public static void main(String[] args)
    {
        int arr[] = { 1, 3, 7, 5, 6, 2 };
        int n = arr.length;
        int arr1[] = {  3, 4, 5, 6, 2 };
        int arr2[] = { 4, 3, 5, 6};
        int arr3[] = { 13, 4, 5, 2 };
        int arr4[] = { 10,33, 4, 12 };
 
        // Function call
        find_small_large_number(arr);
        find_small_large_number(arr1);
        find_small_large_number(arr2);
        find_small_large_number(arr3);
        find_small_large_number(arr4);
    }
}