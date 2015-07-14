/*

	GradeCalculator.java				Java Foundations

	Used to learn concepts within Chapters 3 and 4 in Java Foundations

*/

import java.util.Scanner;

public class GradeCalculator {

	public static void main(String[] args) {

		int assignments, count, assignmentCounter;
		double average, grade, runningTotal = 0;
		String name;

		Scanner keyboard = new Scanner(System.in);

		System.out.print("Enter student's name: ");
		name = keyboard.nextLine();

		System.out.print("Enter the number of assignments: ");
		assignments = keyboard.nextInt();

		//----------------------------------
		//	Loop
		//----------------------------------

		count = 0;
		assignmentCounter = 1;

		while (count < assignments) 
		{			
				System.out.print("Enter the grade for assignment " + assignmentCounter + ":");
				grade = keyboard.nextDouble();
				runningTotal += grade;
				assignmentCounter++;
				count++;
			}

		average = runningTotal / count;

		//----------------------------------
		//	If/else
		//----------------------------------

		if (average >= 90.00)
			System.out.println(name + "'s final grade is " + average);
		else if (average >= 80.00 && average < 90.00)
			System.out.println(name + "'s final grade is " + average);
		else if (average >= 70.00 && average < 80.00)
			System.out.println(name + "'s final grade is " + average);
		else if (average >= 60.00 && average < 70.00)
			System.out.println(name + "'s final grade is " + average);
		else 
			System.out.println(name + "'s final grade is " + average);

	}
}
