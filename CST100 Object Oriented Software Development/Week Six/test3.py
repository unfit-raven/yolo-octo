# Random programs and algorithms, some from homework, some from textbooks

myname = "Edgar Allan Poe"
namelist = myname.split()
init = ""
for aname in namelist:
    init = init + aname[0]
print(init)


# -------------------
# Algorithm workbench
# -------------------

# Write an if statement that assigns 100 to x when y is equal to 0
y = 0
if y == 0:
    x = 100
    print(x)

# Write an if statement that assigns 0 to x when y is equal to 10. Otherwise, x equals 1
if y == 10:
    x = 0
    print(x)
else:
    x = 1
    print(x)

# Write an if-else-if statement that assigns .10, .15, or .20 to commission, depending on the value
# of variable "sales"
sales = 15000
if sales < 10000:
    commission = .10
elif sales > 10000 and sales <= 15000:
    commission = .15
else:
    commission = .20

print(commission)

# Write an if statement that sets the variable "hours" to 10 when the boolean flag
# variable "minimum" is equal to True
minimum = True
if minimum == True:
    hours = 10
    print(hours)
else:
    print("False")

# Write nested if statements that perform the following tests: If amount1 is greater
# than 10 and amount2 is less than 100, display the greater of the two.
# amount1 = int(input("Please enter an integer greater than 10: "))
# amount2 = int(input("Please enter an integer less than 100: "))
amount1 = 55
amount2 = 99
if amount1 > 10 and amount2 < 100:
    if amount1 < amount2:
        print(amount2)
    else:
        print(amount1)

# Write an if statement that prints the message "The number is valid" if the variable
# "grade" is within the range 0 through 100
grade = 3
if grade >= 0 and grade <= 100:
    print("The number is valid")

# Write an if statement that prints the message "The number is valid if the variable
# "temperature" is within the range -50 through 150
temperature = 103
if temperature >= -50 and temperature <= 150:
    print("The number is valid")

# Write an if statement that prints the message "The number is not valid" if the variable
# "hours" is outside the range 0 through 80
#hours = 8
#if hours < 0 and hours > 80:
#    print("The number is not valid")




