/*
	MinOfThree.java

	Demonstrates the use of nested if statements

*/

import java.util.Scanner;

public class MinOfThree {

	public static void main(String[] args) {

		int num1, num2, num3, min = 0;

		Scanner keyboard = new Scanner(System.in);

		System.out.println("Enter three integers: ");
	
		num1 = keyboard.nextInt();
		num2 = keyboard.nextInt();
		num3 = keyboard.nextInt();

		if (num1 < num2)
			if (num1 < num3)
				min = num1;
			else
				min = num3;

				else
				if (num2 < num3)
					min = num2;

				else
					min = num3;

		System.out.println("Minimum value: " + min);
	}
}