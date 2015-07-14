/*
	PP3_5.java
	Write an application that reads the radius of a sphere and prints
	its volume and surface area. Use the following formulas, in which 'r'
	represents the sphere's radius. Print the output to four decimal places.
	Formulas: 
		Volume = 4/3*PI*r^3
		Surface Area = 4*PI*r^2
*/

import java.util.Scanner;

public class PP3_5 {
	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);

		double radius, volume, surfaceArea;
		final double PI = 3.1415;

		System.out.print("This program will read the radius of a sphere\n" + 
							"and calculate its volume and surface area.\n");

		System.out.print("Please enter the radius of a sphere: ");
		radius = keyboard.nextDouble();

		volume = 1.3333 * PI * (Math.pow(radius, 3));		// 4/3 ~ 1.3333
		surfaceArea = 4 * PI * (Math.pow(radius, 2));

		System.out.println("The volume is: " + volume);
		System.out.println("The surface area is: " + surfaceArea); 
	}
}
