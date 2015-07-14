/*
	deathbyloop.java

	Create modified versions of the Stars program to print the following 
	pattern. [15 points]
*/

public class deathbyloop 
{

	public static void main(String[] args) 
	{
            
            /*
            for (int i = 1; i <= 9; i = i + 2)
            {
                  for (int j = 1; j <= i; j++)
                        System.out.print("*");

                  System.out.println();
                  System.out.println();
            }

             for (int i = 9; i >= 1; i = i - 2)
            {
                  for (int j = 1; j <= i; j++)
                        System.out.print("*");

                  System.out.println();
                  System.out.println();
            }

            System.out.println();
            System.out.println();
            */


            for (int i = 1; i <= 9; i += 2)
                  
            {
                  for (int j = 8; j >= i; j -= 2)
                       System.out.print(" ");
                  for (int k = 1; k <=i; k++)
                        System.out.print("*");

                     
                  
                  System.out.println();
                  System.out.println();
            }
          
            for (int i = 9; i >= 1; i -= 2)
                  
            {
                  for (int j = 8; j >= i; j -= 2)
                       System.out.print(" ");
                  for (int k = 1; k <=i; k++)
                        System.out.print("*");
                     

                  System.out.println();
                  System.out.println();
            }


	}
}