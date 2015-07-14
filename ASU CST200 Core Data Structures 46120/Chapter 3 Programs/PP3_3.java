/*
	PP3_3.java
	Write an application that creates and prints a random phone
	number of the form xxx-xxx-xxxx. Include the dashes in 
	the output. Do not let the first three digits contain 
	an 8 or 9 (but don't be more restrictive than that), and 
	make sure that the second set of three digits is not 
	greater than 742. Hint: Think through the easiest way 
	to construct the phone number. Each digit does not have 
	to be determined separately.
*/

import java.util.Random;

public class PP3_3 {
	public static void main(String[] args) {

		Random numberGenerator = new Random();

		int firstAreaDigit, secondAreaDigit, thirdAreaDigit, prefixDigits, lineDigits;

		firstAreaDigit = numberGenerator.nextInt(8);		// No digit in the area code can be
		secondAreaDigit = numberGenerator.nextInt(8);		// an 8 or a 9. Hence individual
		thirdAreaDigit = numberGenerator.nextInt(8);		// creation of each digit in area code.

		prefixDigits = numberGenerator.nextInt(742) + 100;	// Prefix number must be less than 742 
															// and contain 3 digits.
		
		lineDigits = numberGenerator.nextInt(9999) + 1000;	// Line number must be 4 digits 
															// with no other restrictions.
															

		System.out.println(firstAreaDigit + "" + secondAreaDigit + "" + thirdAreaDigit + 
										"-" + prefixDigits + "-" + lineDigits);


	}
}