
////////////////////////////////////////////////////////////////////////////////
// https://www.hackerrank.com/challenges/java-static-initializer-block/problem
// Java Static Initializer Block

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

static boolean flag = true;
static int B, H;
static Scanner sc = new Scanner(System.in);

static {
    B = sc.nextInt();
    H = sc.nextInt();
    if (B <= 0 || H <= 0) {
        flag = false;
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}

	}//end of main

}//end of class

////////////////////////////////////////////////////////////////////////////////
// https://www.hackerrank.com/challenges/java-string-compare/problem
// Java Substring Comparisons

public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        //Arrays.sort(strAr);
        for (int i = 0; i < s.length() - k + 1; i++){

            String subVal = s.substring(i, i + k);
            if (i == 0){
                smallest = subVal;
                largest = smallest;
            }
            if (smallest.compareTo(subVal) > 0 ){
                smallest = subVal;
            }
            if (largest.compareTo(subVal) < 0 ){
                largest = subVal;
            }
        }

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'

        return smallest + "\n" + largest;
        //return Integer.toString(strAr.length);
    }

////////////////////////////////////////////////////////////////////////////////
