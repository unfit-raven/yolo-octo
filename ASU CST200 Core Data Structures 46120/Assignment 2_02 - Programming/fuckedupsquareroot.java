/*
	McKinney_A02Q1.java
	
	Write a program that computes and displays the distance between two points. 
	Use the following formula and prompt the user for four doubles that make up 
	the two points. (Display any number of decimals.) [10 points]:
		Formula: Distance = SquareRootOf((x2-x1)^2 + (y2-y1)^2);
*/

import java.util.Scanner;

public class fuckedupsquareroot {
	
	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);

		double x1, x2, y1, y2;
		double distance;

		System.out.print("This program will read the (x, y) coordinates for\n" +
						"two points and compute the distance between them.\n");
		
		System.out.print("What is x1? ");
		x1 = keyboard.nextDouble();
		System.out.print("What is y1? ");
		y1 = keyboard.nextDouble();
		System.out.print("What is x2? ");
		x2 = keyboard.nextDouble();
		System.out.print("What is y2? ");
		y2 = keyboard.nextDouble();
		
		distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
		System.out.println("Distance between points: " + distance);
		
	}
}