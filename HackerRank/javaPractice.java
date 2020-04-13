
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
//
//
public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
         String Ar = new StringBuilder(A).reverse().toString();

         if (A.equals(Ar)){
             System.out.print("Yes");
         }
         else{
              System.out.print("No");
         }
    }
}

////////////////////////////////////////////////////////////////////////////////
// https://www.hackerrank.com/challenges/java-anagrams/problem
// Java Anagrams

static boolean isAnagram(String a, String b) {
        // Complete the function
        HashMap<String, Integer> dict_A = new HashMap<String, Integer>();
        HashMap<String, Integer> dict_B = new HashMap<String, Integer>();

        if (a.lenght() != b.lenght()){
            return false;
        }

        for(int i = 0; i < a.lenght(); i++){
            String val = Character.toLowerCase(a.charAt(i));
            if(dict_A.get(val)){
                dict_A.put(val, dict_A.get(val) + 1);
            }
            else{
                 dict_A.put(val, 1);
            }
        }

       for(int i = 0; i < b.lenght(); i++){
           String val = Character.toLowerCase(b.charAt(i));
            if(dict_B.get(val)){
                dict_B.put(val, dict_B.get(val) + 1);
            }
            else{
                 dict_B.put(val, 1);
            }
        }

        dict_A.forEach((k, v) -> {
            if(!dict_B.get(k) || dict_B.get(k) != v){
                return false;
            }
        });

        return true;
    }

    // really good one
     static boolean isAnagram(String a, String b) {
        // Complete the function

        if(a.length() != b.length())
            return false;
        int c[] = new int[26];
        int d[] = new int[26] ;
        a = a.toUpperCase();
        b = b.toUpperCase();
        for(int i=0; i<a.length(); i++){
            c[a.charAt(i) - 'A']++;
            d[b.charAt(i) - 'A']++;
        }
        for(int i =0;i<26; i++)
            if(c[i] != d[i] ) return false;
        return true;

    }

    // the best good one -
     static boolean isAnagram(String a, String b) {
        // Complete the function

        if(a.length() != b.length())
            return false;
        int helper_ar[] = new int[26];
        a = a.toUpperCase();
        b = b.toUpperCase();
        for(int i=0; i<a.length(); i++){
            helper_ar[a.charAt(i) - 'A']++;
            helper_ar[b.charAt(i) - 'A']--;
        }
        int sum = 0;
        for(int i =0;i<26; i++){
            sum += helper_ar[i];
        }
        return sum == 0 ? true : false;

    }