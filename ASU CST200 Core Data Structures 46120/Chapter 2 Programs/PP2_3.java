// PP2_3.java			Chapter 2 Programming Project, Java Foundations

public class PP2_3
{
	public static void main(String [] args)
	{
		float x = 5.27f;
		float y = 7.6f;
		float sum, difference, product;

		sum = x + y;
		difference = x - y;
		product = x * y;

		System.out.println("\t\tPrint the sum, difference and product of two " +
							"floating point numbers.");
		System.out.println("Numbers: 5.27 and 7.6\nSum: " + sum + "\nDifference: " + 
							difference + "\nProduct: " + product);

	}
}