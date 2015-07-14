// TempConverter.java		// Java Foundations
//
// Demonstrates the use of primitive date types and 
// arithmetic expressions

public class TempConverter
{
	public static void main(String [] args)
	{
		final int BASE = 32;
		final double CONVERSION_FACTOR = 9.0 / 5.0;

		double fahrenheitTemp;
		int celsiusTemp = 24; // Value to convert

		fahrenheitTemp = celsiusTemp * CONVERSION_FACTOR + BASE;

		System.out.println("Celsius Temperature: " + celsiusTemp);
		System.out.println("Fahrenheit Equivalent: " + fahrenheitTemp);
	}
}