// PP2_4.java		Chapter 2 Programming Project, Java Foundations
//
// Converts user supplied Fahrenheit temp to celsius

import java.util.Scanner;  // Import scanner

public class PP2_4
{
	public static void main(String [] args)
	{

		/* Conversion Formula:
			C = (F-32) * (5/9)
		*/

		int user_temp;  //  Temp to convert, entered by user
		float celsius;	//	Converted temp
		final int BASE = 32;
		final float CONVERSION_FACTOR = 5.0f / 9.0f;

		Scanner scan = new Scanner(System.in);	// Create Scanner object

		System.out.print("Enter the Fahrenheit temperature: ");
		user_temp = scan.nextInt();

		celsius = (user_temp - BASE) * (CONVERSION_FACTOR);

		System.out.println("Fahrenheit temperature: " + user_temp);
		System.out.println("Celsius Equivalant: " + celsius);
	}
}