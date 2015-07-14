import java.util.Scanner;

public class fuckup {
	
	public static void main(String[] args) {

	int count = 0;
	int howmany;
	int numberNumber = 1;
	double number;
	double runningTotal = 0;
	double average;


	Scanner scan = new Scanner(System.in);

	System.out.print("How many numbers will you enter? ");
	howmany = scan.nextInt();

	while (count < howmany)
		{
			System.out.print("Enter number " + numberNumber + ": ");
			number = scan.nextDouble();
			runningTotal += number;
			numberNumber++;
			count++;
		}

	average = runningTotal / count;
	
	System.out.println("You entered " + howmany + " numbers.");
	System.out.println("The total is: " + runningTotal);
	System.out.println("The average is: " + average);


	}
}