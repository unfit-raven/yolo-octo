// McKinney_A01Q4.java
/*
	Q4: Write a program that reads integers representing a time duration in hours, 
	minutes, and seconds, and then prints the equivalent total number of 
	seconds. [10 points]
*/

import java.util.Scanner;		// Import Scanner

public class McKinney_A01Q4
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);		// Create Scanner object called 'scan'

		int hours, minutes, seconds, total_seconds;
		final int HOUR_CONVERSION_RATE = 3600;		// 3600 Seconds in an hour
		final int MINUTE_CONVERSION_RATE = 60;		// 60 seconds in a minute

		System.out.print("Enter the number of hours: ");
		hours = scan.nextInt();

		System.out.print("Enter the number of minutes: ");
		minutes = scan.nextInt();

		System.out.print("Enter the number of seconds: ");
		seconds = scan.nextInt();

		total_seconds = (hours * HOUR_CONVERSION_RATE) + 
						(minutes * MINUTE_CONVERSION_RATE) + seconds;

		System.out.println("The total seconds are " + total_seconds);
	}
}