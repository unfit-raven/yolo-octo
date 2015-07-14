/*
PP3_6.java
	Write an application that reads the lengths of the sides of a 
	triangle from the user. Compute the area of the triangle 
	using Heron's formula (below), in which 's' represents
	half of the perimeter of the triangle, and a, b, c represent the
	lengths of the three sides. Print the area to three decimal places.
		Formula: Area = SquareRootOf(s(s-a)(s-b)(s-c))
				 Perimeter = a + b + c
*/

import java.util.Scanner;

public class PP3_6 {
	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);

		double sideA, sideB, sideC, halfPerimeter;		
		double area;

		System.out.println("This program will calculate the area of a triangle." + 
						"\nThe user will enter each length of the triangle's three" +
						" sides separately.");
		
		System.out.print("Please enter the length of side A: ");
		sideA = keyboard.nextDouble();
		System.out.print("Please enter the length of side B: ");
		sideB = keyboard.nextDouble();
		System.out.print("Please enter the length of side C: ");
		sideC = keyboard.nextDouble();

		halfPerimeter = (sideA + sideB + sideC) * 0.5;		// Calculate half of the triangle's perimeter. 

		area = Math.sqrt(halfPerimeter * (halfPerimeter - sideA) * (halfPerimeter - sideB) * (halfPerimeter - sideC));

		System.out.println("The area of the triangle is: " + area);

	}
}

