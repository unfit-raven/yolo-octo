# Second FizzBuzz solution
# For numbers 1 through 100, determine if it is
# divisible by 3. If it is, print Fizz. If it is
# divisible by 5, print Buzz. If it is divisible
# by both 3 and 5, print FizzBuzz.

for number in range(1, 101):
    if number % 15 == 0:
        print("The number", number, "is divisible by both "
                                    "3 and 5. FizzBuzz!")
    elif number % 3 == 0:
        print("The number", number, "is divisible by 3. Fizz!")
    elif number % 5 == 0:
        print("The number", number, "is divisible by 5. Buzz!")
    else:
        print("The number", number, "is not divisible by "
                                    "either 3 or 5.")
