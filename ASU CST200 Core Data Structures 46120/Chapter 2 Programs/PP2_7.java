// PP2_7.java		Chapter 2 Programming Projects, Java Foundations
//
// Convert a value representing seconds to hours, minutes and seconds

/*
	$init = 685;
	$hours = floor($init / 3600);
	$minutes = floor(($init / 60) % 60);
	$seconds = $init % 60;
*/

import java.util.Scanner;

public class PP2_7
{
	public static void main(String [] args)
	{
		Scanner scan = new Scanner(System.in);		// Create Scanner object named 'scan'

		int total_seconds;
		int seconds;
		int minutes;
		int hours;
		final int HOUR_CONVERSION = 3600;
		final int MINUTE_CONVERSION = 60;

		System.out.print("Enter a number of seconds: ");
		total_seconds = scan.nextInt();

		hours = total_seconds / HOUR_CONVERSION;
		minutes = (total_seconds / MINUTE_CONVERSION) % 60;
		seconds = total_seconds % 60;

		System.out.println(total_seconds + " seconds is equivalent to " + hours + " hours " + 
										minutes + " minutes " + seconds + " seconds.");

	}
}
