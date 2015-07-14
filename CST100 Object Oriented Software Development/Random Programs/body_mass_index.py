# Write a program that calculates and displays a persons body mass index.
# Optimal is 18.5 to 25
# Underweight is less than 18.5
# Overweight is greater than 25

weight = int(input("Please enter your weight in pounds: "))
height = int(input("Please enter your height in inches: "))

BMI = weight * 703/height**2

if BMI < 18.5:
    print("You are underweight. ")
elif BMI >= 18.5 and BMI <= 25:
    print("You are at an optimal weight.")
elif BMI > 25:
    print("You are overweight.")




