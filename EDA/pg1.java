import java.io.*;
import java.util.*;
 
class pg1{
 
    // Function to find the missing number
    public static void findMissing(int arr[], int N)
    {
        int i;
        int temp[] = new int[N + 1];
        for (i = 0; i <= N; i++) {
            temp[i] = 0;
        }
 
        for (i = 0; i < N; i++) {
            temp[arr[i] - 1] = 1;
        }
 
        int ans = 0;
        for (i = 0; i <= N; i++) {
            if (temp[i] == 0)
                ans = i + 1;
        }
        System.out.println(ans);
    }
    // Driver Code
    public static void main(String[] args)
    {
        int arr[] = { 1, 3, 7, 5, 6, 2 };
        int n = arr.length;
        int arr1[] = { 1, 3, 4, 5, 6, 2 };
        int arr2[] = { 4, 3, 7, 5, 6, 2 };
        int arr3[] = { 1, 3, 4, 5, 6, 2 };
        int arr4[] = { 1, 3, 7, 4, 6, 2 };
 
        // Function call
        findMissing(arr, n);
        findMissing(arr1, arr1.length);
        findMissing(arr2, arr2.length);
        findMissing(arr3, arr3.length);
        findMissing(arr4, arr4.length);
    }
}