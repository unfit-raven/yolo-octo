// PP2_6.java		Chapter 2 Programming Projects
//
// Write a program that reads hours, minutes and seconds inputed from the 
// user and converts to total seconds
	
import java.util.Scanner;		

public class PP2_6
{
	public static void main(String [] args)
	{
		Scanner scan = new Scanner(System.in);		// Create Scanner object called 'scan'

		int hours, minutes, seconds, total_seconds;
		final int HOUR_CONVERSION_RATE = 3600;
		final int MINUTE_CONVERSION_RATE = 60;

		System.out.print("Enter the number of hours: ");
		hours = scan.nextInt();

		System.out.print("Enter the number of minutes: ");
		minutes = scan.nextInt();

		System.out.print("Enter the number of seconds: ");
		seconds = scan.nextInt();

		total_seconds = (hours * HOUR_CONVERSION_RATE) + 
												(minutes * MINUTE_CONVERSION_RATE) + seconds;

		System.out.println(hours + " hours " + minutes + " minutes " + seconds + 
							" seconds is equivalent to " + total_seconds + " seconds.");

	}
}