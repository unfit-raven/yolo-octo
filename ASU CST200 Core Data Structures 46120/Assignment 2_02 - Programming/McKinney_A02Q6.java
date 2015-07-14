/*
	McKinney_A02Q6.java

	Create modified versions of the Stars program to print the following 
	pattern. [15 points]
*/

public class McKinney_A02Q6 
{

	public static void main(String[] args) 
	{

		    
            for (int i = 1; i <= 9; i += 2) // First major loop, must increment by 2
                                            // Used to create upper half of diamond
            {
                  for (int j = 8; j >= i; j -= 2) 
                       System.out.print(" ");
                  for (int k = 1; k <=i; k++)
                        System.out.print("*");

                  System.out.println();
                  System.out.println();
            }
          
            for (int i = 9; i >= 1; i -= 2) // Second major loop, essentially same first loop but reversed
                                            // Used to create lower half of diamond
            {
                  for (int j = 8; j >= i; j -= 2) // Nested loops here are same as above
                       System.out.print(" ");
                  for (int k = 1; k <=i; k++)
                        System.out.print("*");
                     
                  System.out.println();
                  System.out.println();
            }

	}
}