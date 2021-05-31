// # Perfect Sum Problem (Print all subsets with given sum)
// # Difficulty Level : Hard
// # Last Updated : 02 Mar, 2021
// # Given an array of integers and a sum, the task is to print all subsets of the given array with a sum equal to a given sum.
// # Examples: 

// # Input : arr[] = {2, 3, 5, 6, 8, 10}
// #         sum = 10
// # Output : 5 2 3
// #          2 8
// #          10

// # Input : arr[] = {1, 2, 3, 4, 5}
// #         sum = 10
// # Output : 4 3 2 1 
// #          5 3 2 
// #          5 4 1

// Java code to find the number of
// possible subset with given sum
import java.util.*;
import java.lang.*;
import java.io.*;
 
class GFG {
     
    static int count;
    static int sum;
    static int n;
     
    // Driver code
    public static void main (String[] args) {
        count = 0;
        n = 5;
        sum = 10;
 
        int[] pat = {2, 3, 5, 6, 8, 10};
         
        f(pat, 0, 0);
         
        System.out.println(count);
    }
     
    // Function to select or not the array element
    // to form a subset with given sum
    static void f(int[] pat, int i, int currSum) {
        if (currSum == sum) {
            count++;
            return;
        }
        if (currSum < sum && i < n) {
            f(pat, i+1, currSum + pat[i]);
            f(pat, i+1, currSum);
        }
    }
}
