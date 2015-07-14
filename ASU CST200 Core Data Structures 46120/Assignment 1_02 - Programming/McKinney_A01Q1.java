// McKinney_A01Q1.java
/*
	Q1: Download the attached program, A01_02_bugged.java and try running it in Java. 
	The program contains a total of 5 errors (a combination of compile-time errors and 
	logical errors). Debug the program to identify and rectify all the errors.  
	For each bug fixed, explain it and list its general type. Below are the expected 
	results.  Hint: look at the spacing in the output - details are important. [15 points]
*/

import java.util.Scanner;

public class McKinney_A01Q1 
{
    public static void main(String[] args)		// Removed constant variable 'final int NUM'
    											// from main method. Also removed duplicate
    											// 'public static' and changed formatting
    {
    	Scanner scan = new Scanner(System.in);       
		
		int input, result;
    	final int NUM = 2;			// Constant NUM originally assigned value of 1. Changed to 2
    								// in order to resolve logical error. 

		System.out.print("Enter any number: ");		// Changed parameter to match expected formatting
    	input = scan.nextInt();		// Scanner originally looked for string input due to'nextLine' 
    								// when 'input' variable is an integer type. Resulted in a compile-time error.
    				
	
		result = input % NUM;		// Added missing semi-colon to resolve compile-time error.

		if (result == 0) 			// Code was 'result = 0' which is an assignment. Resulted in compile-time error.
			{
				System.out.println("Number " + input + " is even.");	// Changed order of 'even/odd' in print
			}															// statements to resolve logical error.
		else if (result != 0) 											// Also removed new line escape characters
			{															// and used 'println' to resolve formatting
				System.out.println("Number " + input + " is odd.");		
			}															
    }    
}

