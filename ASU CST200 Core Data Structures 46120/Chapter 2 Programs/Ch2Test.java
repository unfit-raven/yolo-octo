// Ch2Test.java		// Random program written from chapter 2 of Java Foundations

import java.util.Scanner;

public class Ch2Test
{
	public static void main(String [] args)
	{

		Scanner scan = new Scanner(System.in);

		int var_one = 5;
		int var_two = 10;
		int var_three = 11;
		int answer;

		byte small_num = 100;

		final int MAX_OCCUPANCY = 427; // cannot change value now that it's a constant - compiler will freak


		answer = (var_one + var_two + var_three) / 3;	// "int" variable type will not result in an accurate 
														// number - no decimal point! would need "float" or
														// "double" type for decimal point.

		System.out.println("The average of " + var_one + " plus " + var_two + " plus " + var_three +
							" equals about " + answer);		// see? no decimal point! okay for approximation though
		
		System.out.println();	// used for white space

		System.out.println("The maximum occupancy is " + MAX_OCCUPANCY); // these "int" variable types are automatically
																		 // converted to strings and concatenated, then 
																		 // passed to the "println" method when used 
																		 // this way
		System.out.println("What's the maximum value a \"byte\" variable type can hold?");
		System.out.println("It's 127! That's pretty damn small! Here's what our \"small_num\"" +
							" variable holds: " + small_num);

		System.out.println();

		System.out.println("-----------------------Char variable type-----------------------");
		// USING CHARACTER VARIABLE TYPES! :)
		
		char h = 'H';
		char e = 'e';
		char l = 'l';
		char  o = 'o';
		char point = '!';

		System.out.println(h + "" + e + "" + l + "" + l + "" + o + "" + point);
		System.out.println(h + e + l + l + o + point);

		System.out.println();	// white space

		
		System.out.println("---------------------Casting/Conversion techniques---------------");
		// Conversion techniques

		float money = 25.5f;
		int dollars = 25;

		System.out.println("Money: " + money);
		System.out.println("Dollars: " + dollars);

		float result;
		int total = 25;
		int count = 11;
		result = total / count; // will perform integer devision and discard decimal point/remainder
		System.out.println(result);

		result = (float) total / count;	// casting total to a float type will provide a decimal point
		System.out.println(result);

		//int test_int = 12.6;	// Purposely assigning floating point value type to int variable type
								// in hopes of seeing a compiler error
								// Success! Found 1 error - "required: int    	found: double"
		System.out.println();

		System.out.println("--------------------------Modulo/Remainder------------------------------");
		int remainder;
		int division;
		division = 19 / 5;
		remainder = 19%5;
		System.out.println("\t\tInteger Division!\nDivision: 19/5 is: \n\t" + division + "\nRemainder: " +
						"of 19/5 is: \n\t" + remainder);

		System.out.println();

		System.out.println("--------------------------Division by zero-----------------------------");
		//int some_random_number = 5;
		//int divided_by_zero;
		//divided_by_zero = some_random_number / 0;

		System.out.println();	// White space

		System.out.println("--------------------------Area of a Circle---------------------------");
		float area_of_circle;
		float pi = 3.14f;
		float incorrect_pi = 4.14f;
		int radius = 5;
		area_of_circle = pi * (radius * radius);
		System.out.println("Area is: " + area_of_circle);
		System.out.println("Area is: "+ (incorrect_pi * radius * radius));

		System.out.println();		//White space

		System.out.println("--------------------------Short answer test-----------------------");

		System.out.println ("Here we go!");

		System.out.println ();

		System.out.print ("You could always run this in Java to double check your answer.");

		System.out.println ("12345");

		System.out.print ("Another.");

		System.out.println ("Finally done.");

		System.out.println("---------------------------------------------------------------");

		System.out.println();
		System.out.println("He thrusts his fists\n\tagainst" +
							" the post\nand still insists\n\the sees the \"ghost\"");
	}
								
}
