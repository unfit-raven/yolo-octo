/*
	PP3_2.java
	Write an application that prints the sum of cubes.
	Prompt for and read two integer values and print
	the sum of each value raised to the third power.
*/

import java.util.Scanner;

public class PP3_2 {
	public static void main(String [] args) {

		Scanner keyboard = new Scanner(System.in);

		int valueOne, valueTwo;
		double totalSum;

		System.out.print("This program will prompt for two integers amd calculate\n" +
							"the sum of their cubes.\n");

		System.out.print("Please enter the first integer: ");
		valueOne = keyboard.nextInt();
		System.out.print("Please enter the second integer: ");
		valueTwo = keyboard.nextInt();

		totalSum = Math.pow(valueOne, 3) + Math.pow(valueTwo, 3);
		System.out.println("The sum of cubes equals " + totalSum);

	}
}