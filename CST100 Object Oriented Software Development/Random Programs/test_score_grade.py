# Write a program that has variables to hold three test scores.
# The program should ask the user to enter three test scores
# and then assign the values to a variable. The program should
# display the average of the test scores and the letter grade
# that is assigned for the score average.
# 90-100 = A, 80-89 = B, 70-79 = C, 60-69 = D, below 60 = F

test1 = eval(input("Please enter the score for test 1: "))
test2 = eval(input("Please enter the score for test 2: "))
test3 = eval(input("Please enter the score for test 3: "))

average = (test1 + test2 + test3)/3

if average >= 90:
    print("The letter grade is A.")
elif average >= 80 and average <= 89:
    print("The letter grade is B.")
elif average >= 70 and average <= 79:
    print("The letter grade is C.")
elif average >= 60 and average <= 69:
    print("The letter grade is D.")
elif average > 60:
    print("The letter grade is F.")