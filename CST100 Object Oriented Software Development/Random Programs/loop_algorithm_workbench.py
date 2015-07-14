from fractions import Fraction
# import json
import random

# Write a loop that lets the user enter a number. The number
# should be multiplied by 10, and the result stored in the
# variable "product". The loop should iterate as long as
# "product" contains a value less than 100.

# print("This loop will continue until a number multiplied by 10 equals over 100.")
# user_input = eval(input("Please enter a number: "))
# product = user_input * 10
#
# while product < 100:
# user_input = eval(input("Please enter another number: "))
#     product = user_input * 10
#
# print("The product of", user_input, "and 10 is", product, "and the "
#                                                           "loop has stopped")

# Write a loop that asks the user to enter two numbers. The
# numbers should be added and the sum displayed. The loop
# should ask the user whether or not to perform the
# operation again. If so, the loop should repeat - if not,
# the loop should terminate.

# Set user_input to "y" to start loop
# user_input = "y"
#
# while user_input == "y":
#     first_number = eval(input("Please enter the first number: "))
#     second_number = eval(input("Please enter the second number: "))
#     sum = first_number + second_number
#     print("The sum is", sum)
#     user_input = input("Would you like to continue? Please enter Y for yes or N for no. ").lower()
#
# print("You have stopped the loop.")

# Write a loop that displays the following set of numbers:
# 0, 10, 20, 30...1000

for i in range(0, 1010, 10):
    print(i)

# Write a loop that asks the user to enter a number. The loop should
# iterate 10 times and keep a running total of the numbers entered.

# print("This loop will iterate 10 times.")
# total = 0
# for i in range(10):
#     number = eval(input("Please enter a number: "))
#     total += number
#
# print("The loop has finished, and the sum of all numbers "
#       "entered is ", total)

# Write a for loop that calculates the total of the following series
# of numbers: 1/30, 2/29, 3/28, 4/27...30/1.

print(sum(Fraction(n, 31 - n) for n in range(1, 31)))

fraction_sum = 0
for n in range(1, 31):
    fraction_sum += Fraction(n, 31 - n)
print(fraction_sum)

# Write a nested loop that displays 10 rows of * characters
# There should be 15 # characters in each row.

for i in range(10):
    for j in range(15):
        print("#", end=" ")
    print()

# Convert the while loop below into a do while loop
# Not possible in python?

# x = 1
# while x > 0:
#     x = eval(input("Please enter a number: "))
# print("Yep, the loop ends after inputting a number equal to "
#       "or less than 0")

# Write an input validation loop that asks the user to enter a
# number in the range of 1 through 4

# x = 0
# while x < 1 or x > 4:
#     x = eval(input("Please enter a number between 1 and 4: "))
#
# print("Thank you for entering a suitable value.")

# Write an input validation loop that asks the user to enter the word
# "yes" or "no"

# user_input = input("Please enter 'yes' or 'no': ").lower()
# while user_input != "yes" and user_input != "no":
#     user_input = input("Incorrect word. Please enter 'yes' or 'no': ").lower()
# print("Thank you for entering a suitable word.")

# for i in range(8):
#     for j in range(8):
#         print("#", end=" ")
#     print()

# Add all consecutive integers from 1 to 100, 1 to 1000, and
# 1 to 1,000,000 and print the result

print("The sum of all integers from 1 to 100 is:")
sum = 0
for num in range(1, 101):
    sum += num
print(sum)

print("The sum of all integers from 1 to 1000 is:")
sum = 0
for num in range(1, 1001):
    sum += num
print(sum)

print("The sum of all integers from 1 to 1,000,000 is:")
sum = 0
for num in range(1, 1000001):
    sum += num
print(sum)

# Add the sum of all even integers from 1 to 1000

print("The sum of all even integers from 1 to 1000 is:")
sum = 0
for num in range(1001):
    if num % 2 == 0:
        sum += num
print(sum)

# Nested loop, wider at top, narrows at bottom.
range_value = 8
for i in range(8):
    range_value -= 1
    for j in range(range_value):
        print("#", end=" ")
    print()

# Write a program so that it displays a random integer in the range
# of 1 through 10

print("This program will display a random integer in the range of "
      "1 through 10 ten times.")
for i in range(10):
    rand = random.randint(1, 10)
    print(rand, ";", end=" ")

print("\n")

# Write a program so that it generates a random number that is either 1
# or 0, and displays the word "yes" or the word "no" depending on
# the number that was generated.

print("This program will randomly generate either a 0 or a 1. "
      "0 will result in the word 'no' printing, and 1 will result in 'yes'.")
print()
rand = random.randint(0, 1)
if rand == 0:
    print("No, the number was", rand)
elif rand == 1:
    print("Yes, the number was", rand)

print()

# Write code that opens one file and copies its contents to another file.
#
# print("Opening files....")
# infile = open("read_from.txt", "r")
# outfile = open("write_to.txt", "w")
#
# print("Writing contents....")
# aline = infile.readline()
# while aline:
#     outfile.write(aline)
#     aline = infile.readline()
#
# infile.close()
# outfile.close()
# print("Contents written....files closed.")

# Write code that does the following: opens a file named NumbersList.txt, uses a
# loop to write the numbers 1 through 100 to the file, and then closes the file.

# outfile = open("NumbersList.txt", "w")
#
# x = 10 + 20
# y = str(x)
#
# json.dumps(x, "NumbersList.txt")
#
# outfile.close()


# Write code that does the following: opens the NumbersList.txt file that was
# created by the code above, reads all the numbers from the file and displays
# them, and then closes the file.

# Modify the code above so that it adds all the numbers read from the file
# and displays their total.

# Write code that opens a file named NumbersList.txt for writing, but does not
# erase the files contact if it already exits.

# Write a program that asks the user for a positive nonzero integer value.
# The program should use a loop to get the sum of all integers from 1 up to
# the number entered. For example, if the user enters 50, the loop will find
# the sum of 1, 2, 3, 4, ...50.

# Get a number from user
number = int(input("Please enter a positive nonzero integer: "))

sum = 0 # Empty variable declared to hold sum

# Loop to add each number
for num in range(1, number+1):  # Iterate from 1 through the variable "number"
    sum += num  # Add each number (num) from 1 to the "number" to "sum"

print("The total of 1 through", number, "is", sum)

print()

# Write a program that asks the user for a positive integer no greater than
# 15. The program should display a square on the screen using the character
# "X". The number entered by the user will be the length of each side of the
# square.

# Get input from user
print("This program will display a square whose size will depend on a number.")
number = int(input("Please enter a positive nonzero integer "
                   "between 1 and 15: "))

print()  # Just to create space

# Nested loop to create square
for i in range(number):
    for j in range(number):
        print("X", end=" ")
    print()
