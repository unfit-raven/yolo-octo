// PP2_1.java		Chapter 2 Programming Project, Java Foundations

public class PP2_2
{
	public static void main(String [] args)
	{
		// Write an application that reads three integers and 
		// prints their average

		int int_one = 2, int_two = 5, int_three = 1;
		int total;
		float average;

		total = int_one + int_two + int_three;

		average = (float) total / 3;

		System.out.println("Add three integers and show the average. \nIntegers:" +
							" 2, 5, and 1.\nTotal: " + total + "\nAverage: " + average);
	}
}