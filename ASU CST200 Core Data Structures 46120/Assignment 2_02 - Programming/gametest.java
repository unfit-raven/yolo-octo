/*
    McKinney_A02Q5.java

    Write a program that plays the Hi-Lo guessing game with numbers. 
    The program should pick a random number between 1 and 100 
    (inclusive), then repeatedly prompt the user to guess the number. 
    On each guess, report to the user that they are correct or that 
    the guess is high or low. Continue accepting guesses until the user 
    guesses correctly or chooses to quit. A user may choose to quit 
    midgame by entering 0. Count the number of guesses and report that 
    value when the user guesses correctly. At the end of each game 
    (by quitting or a correct guess), prompt to determine whether the 
    user wants to play again. Continue playing games until the user 
    chooses to stop. [20 points]

    */

import java.util.*;     // For Scanner and Random classes

public class gametest {

    public static void main(String[] args) {

        int guess;          // Guess by user
        int number;         // Randomly generated number

        Scanner keyboard = new Scanner(System.in);

        System.out.println("Guess the number! Pick an integer between" +
                            " 1 and 100 to start, and enter 0 to quit.\n");
        System.out.print("What number do you guess? ");
        guess = keyboard.nextInt();

        Random rand = new Random();
        number = rand.nextInt(100) + 1;

        int count = 1;
        while (guess != number && guess != 0)
        {
            if (guess > number)
                System.out.println("That's too high!");
            else if 
                (guess < number)
                System.out.println("That's too low!");

            System.out.print("What number do you guess? ");
            guess = keyboard.nextInt();

            count++;    
        }
            
        if (guess == 0)
            System.out.println("You've quit the game.");
        else 
            System.out.println("That's correct! You've made " + count + 
                                " guesses.");

    }
}