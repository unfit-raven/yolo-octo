/*	Write an application that prompts for and reads the user's first
name and last name (separately). Then print a string composed of the 
first letter of the user's first name, followed but the first five 
characters of the user's last name, followed by a random number in the
range of 10-99. Assume that the last name is at least five letters long.
Similar algorithms are sometimes used to generate usernames for new 
computer accounts. 
*/

import java.util.Scanner;
import java.util.Random;

public class PP3_1 {
	public static void main (String[] args) {

		// Create a Scanner class object
		Scanner keyboard = new Scanner(System.in);
		// Create a Random class object
		Random randNumber = new Random();

		String firstName, lastName, subFirstName, subLastName, username;
		int userNumber;

		System.out.println("This program will create your username.\n" +
							"Please follow the prompts below.\n");

		System.out.print("Please enter your first name: ");
		firstName = keyboard.nextLine();
		System.out.print("Please enter your last name: ");
		lastName = keyboard.nextLine();

		userNumber = randNumber.nextInt(100) + 10;	// Range 10-99

		subFirstName = firstName.substring(0, 1);		// Get first character
		subLastName = lastName.substring(0, 5);		// Get first 5 characters

		username = subFirstName + subLastName + userNumber;
		username = username.toLowerCase();
		System.out.println(username);
	}
}