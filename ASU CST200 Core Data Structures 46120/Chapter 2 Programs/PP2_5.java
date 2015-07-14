// PP2_5.java		Chapter 2 Programming Project, Java Foundations
//
// Convert miles to kilometers, with mile input from user

import java.util.Scanner;

public class PP2_5
{
	public static void main(String [] args)
	{
		Scanner scan = new Scanner(System.in);	// Create Scanner object named 'scan'

		float miles;							// value to convert, entered from user
		float total_kilometers;			
		final float KILOMETER = 1.60935F;		// Kilometers in a mile

		System.out.print("Enter the number of miles: ");
		miles = scan.nextFloat();

		total_kilometers = miles * KILOMETER;

		System.out.println("Miles: " + miles);
		System.out.println("Kilometers: " + total_kilometers);

	}
}