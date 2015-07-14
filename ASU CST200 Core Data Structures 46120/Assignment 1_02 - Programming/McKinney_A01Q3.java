// McKinney_A01Q3.java
/*
	Q3: Create a version of the TempConverter program (slide 35, chapter 2) 
	to convert from Fahrenheit to Kelvin. Read the Fahrenheit temperature 
	from the user. [10 points]
*/

import java.util.Scanner;  // Import scanner

public class McKinney_A01Q3
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);		// Create Scanner object called 'scan'

		/* 
			Conversion Formula: K = (F + 459.67) * 5 / 9
		*/

		int user_temp;  							//  Temp to convert, entered by user
		float kelvin;								//	Converted temp
		final float BASE = 459.67f;
		final float CONVERSION_FACTOR = 5f / 9f;

		System.out.print("Enter Fahrenheit temperature: ");
		user_temp = scan.nextInt();

		kelvin = (user_temp + BASE) * CONVERSION_FACTOR;

		System.out.println("Fahrenheit temperature: " + user_temp);
		System.out.println("Equivalent Kelvin temperature: " + kelvin);
	}
}
