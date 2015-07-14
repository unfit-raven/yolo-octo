package com.example.gradecalculator;

/**
 * Created by robertmckinney on 7/14/15.
 */

import java.util.Scanner;

public class GradeCalculator {

    public static void main(String[] args) {

        int assignments, count, assignmentNumber;
        double calc;
        double enteredGrade = 0;
        String name;

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter student's name: ");
        name = keyboard.nextLine();

        System.out.print("Enter the number of assignments: ");
        assignments = keyboard.nextInt();

        count = 1;
        assignmentNumber = 1;
        for (int i = 1; i <= assignments; i++ )
        {
            System.out.print("Enter grade for assignment " + assignmentNumber + ": ");
            enteredGrade = keyboard.nextDouble();
            enteredGrade += enteredGrade;
            count++;
            assignmentNumber++;
        }

        calc = enteredGrade / count;

        System.out.println("enteredGrade: " + enteredGrade);
        System.out.println("count: " + count);
        System.out.println(name + "'s grade is " + calc);




    }
}
