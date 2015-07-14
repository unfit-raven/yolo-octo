// StringClass.java			Java Foundations
//
// Testing the String class and its methods.

public class StringClass {

	public static void main(String[] args) {

		/* We do not need to import the String class like we 
		   do with the Scanner class. It's imported or packaged
		   by default like integer, enum, etc. However, we could 
		   use the "new" operator and call the constructor, like
		   String title = new String("Java Foundations");
		*/

		   String testString = "This is only a test. Again, this is only a test.";
		   String uppercaseString, lowercaseString;
		   String mutation1, mutation2, mutation3;
		   char methodString;
		   int stringLength;

		   System.out.println("The test String is: " + testString);
		   System.out.println("Now, we'll return the character at the 5th index.");
		   System.out.println("That character should be \'i\'");

		   methodString = testString.charAt(5);
		   System.out.println(methodString);

		   System.out.println("Excellent. Now, let's see how long that string is.");

		   stringLength = testString.length();
		   System.out.println("The String is: " + stringLength + " characters long.");

		   System.out.println("Cool. Now, if we can convert that String to uppercase" + 
		   						" and lowercase letters.");
		   
		   uppercaseString = testString.toUpperCase();
		   lowercaseString = testString.toLowerCase();

		   System.out.println(uppercaseString);
		   System.out.println(lowercaseString);

		   System.out.println("Awesome. Now, let's replace every instance of \'t\' with" +
		   						" \'X'. \nAnd, let's use the uppercase String.");

		   mutation1 = uppercaseString.replace('I', 'X');
		   mutation2 = mutation1.replace('T', 'Z');

		   System.out.println(mutation1);
		   System.out.println(mutation2);

		   mutation3 = testString.concat("\n...well, unless it's not. Then it's not a test.");
		   System.out.println(mutation3);

	}
} 