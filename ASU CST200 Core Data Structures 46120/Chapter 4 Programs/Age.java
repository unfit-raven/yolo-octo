/*
	Age.java			Java Foundations

	Demonstrates the use of an if statement.
*/

import java.util.Scanner;

public class Age {
	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);

		final int MINOR = 21;
		int age;

		System.out.print("Enter your age: ");
		age = keyboard.nextInt();

		if (age < MINOR)
			System.out.println("Youth is a wonder thing. Enjoy.");

		System.out.println("Age is a stage of mind.");
	}
}