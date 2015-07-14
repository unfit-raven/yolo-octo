/*
	PP3_4.java
	Write an application that reads the (x, y) coordinates for 
	two points. Compute the distance between the two points 
	using the following formula:
		Distance = SquareRootOf((x2-x1)^2 + (y2-y1)^2);
*/

import java.util.Scanner;

public class PP3_4 {
	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);

		int x1, x2, y1, y2;
		double distance;		// Both Math methods used require a 'double' type value

		System.out.print("This program will read the (x, y) coordinates for\n" +
						"two points and compute the distance between them.\n");
		
		System.out.print("Please enter the first \'x\' coordinate: ");
		x1 = keyboard.nextInt();
		System.out.print("Please enter the first \'y\' coordinate: ");
		y1 = keyboard.nextInt();
		System.out.print("Please enter the second \'x\' coordinate: ");
		x2 = keyboard.nextInt();
		System.out.print("Please enter the second \'y\' coordinate: ");
		y2 = keyboard.nextInt();
		
		// Math.pow(double num, double power), and Math.sqrt (double num)
		// Formula: Distance = SquareRootOf((x2-x1)^2 + (y2-y1)^2);
		distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
		System.out.println("Distance between points: " + distance);
		


	}
}