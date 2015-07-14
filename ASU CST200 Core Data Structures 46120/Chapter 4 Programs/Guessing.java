/*
	Guessing.java			Java Foundations

	Demonstrates the use of a block statement in an if-else
*/

import java.util.*;

public class Guessing {

	 public static void main(String[] args) {

	 	final int MAX = 10;
	 	int answer, guess;

	 	Scanner keyboard = new Scanner(System.in);
	 	Random rand = new Random();

	 	answer = rand.nextInt(MAX) +1;

	 	System.out.print("I'm thinking of a number between 1 and " +
							+ MAX + ". Guess what it is: ");
	 	guess = keyboard.nextInt();

	 	if (guess == answer)
	 		System.out.println("You got it! Good guessing!");
	 	else 
	 	{
	 		System.out.println("That was not correct, sorry.");
	 		System.out.println("The number was " + answer);
	 	}
	 }
} 