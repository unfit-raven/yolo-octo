// GasMileage.java			Java Foundations
//
// Demonstrates the use of the Scanner class to read numeric data

import java.util.Scanner;

public class GasMileage
{
	// Calculates fuel efficiency based on values entered by 
	// the user

	public static void main(String [] args)
	{
		int miles;
		float gallons, mpg;

		Scanner scan = new Scanner(System.in);

		System.out.print("Enter the number of miles: ");
		miles = scan.nextInt();

		System.out.print("Enter the gallons of fuel used: ");
		gallons = scan.nextFloat();

		mpg = miles / gallons;

		System.out.println("Miles Per Gallon: " + mpg);
	}
}