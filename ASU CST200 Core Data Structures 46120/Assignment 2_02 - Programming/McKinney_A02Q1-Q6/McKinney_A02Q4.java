/*
	McKinney_A02Q4.java

	Write a program that reads an integer value representing a year 
	from the user. The purpose of the program is to determine if the 
	year is a leap year (and therefore has 29 days in February) in 
	the Gregorian calendar. A year is a leap year if it is divisible 
	by 4, unless it is also divisible by 100 but not 400. Produce an 
	error message for any input value less than 1582 (the year the 
	Gregorian calendar was adopted). [10 points]
*/

import java.util.Scanner;

public class McKinney_A02Q4 {

	public static void main(String[] args) {

		int year; 		// Year entered by user

		Scanner keyboard = new Scanner(System.in);

		System.out.print("What year should be checked? ");
		year = keyboard.nextInt();

		if (year < 1582)		// Year must be greater than 1582
			System.out.println("Error - year must be 1582 or later.");
		else
			if (year % 100 == 0 && year % 400 != 0)	// Condition created per instructions above
				System.out.println(year + " is not a leap year.");
			else
				if (year % 4 == 0)
					System.out.println(year + " is a leap year.");
				else
					System.out.println(year + " is not a leap year.");

	}
}
