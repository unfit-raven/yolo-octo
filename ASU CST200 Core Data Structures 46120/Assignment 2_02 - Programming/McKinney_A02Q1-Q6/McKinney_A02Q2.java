/*
	McKinney_A02Q2.java

	Write an application that reads the lengths of the sides of a 
	triangle from the user, and prints its area. The formula is 
	shown below, where s represents half of the perimeter of the 
	triangle, and a, b, and c represent the lengths of the three 
	sides. Print the area to three decimal places. [10 points]
		Formula: Area = SquareRootOf(s(s-a)(s-b)(s-c))
*/

import java.text.DecimalFormat;
import java.util.Scanner;

public class McKinney_A02Q2 {
	
	public static void main(String[] args) {

		double sideA, sideB, sideC, halfPerim; // 'halfPerim' is half of the triangle's perimeter.
		double area;						   // Calculated area of triangle

		System.out.println("This program will calculate the area of a triangle using\n." + 
						"Heron's formula. The user will enter each length of the triangle's\n" +
						"three sides separately.");
		
		Scanner keyboard = new Scanner(System.in);

		System.out.print("What is the length of side a? ");
		sideA = keyboard.nextDouble();
		System.out.print("What is the length of side b? ");
		sideB = keyboard.nextDouble();
		System.out.print("What is the length of side c? ");
		sideC = keyboard.nextDouble();
	
		halfPerim = (sideA + sideB + sideC) * 0.5;	// Calculates half of the triangle's perimeter.

		// Calculates area of triangle using Heron's formula above
		area = Math.sqrt(halfPerim * (halfPerim - sideA) * (halfPerim - sideB) * (halfPerim - sideC));

		System.out.println("You entered " + sideA + " for the length of side a.");
		System.out.println("You entered " + sideB + " for the length of side b.");
		System.out.println("You entered " + sideC + " for the length of side c.");
		
		DecimalFormat formatter = new DecimalFormat("0.###");	// Round to 3 decimal places. 

		// Formatting triangle's perimeter output as well for consistency. 
		System.out.println("Half of the triangle's perimeter is: " + formatter.format(halfPerim));
		System.out.println("The area of the triangle is: " + formatter.format(area));

	}
}

