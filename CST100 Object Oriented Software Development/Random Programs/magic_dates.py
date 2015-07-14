# Write a program that asks the user to enter a month (in numeric form),
# a day, and a two digit year. The program should then determine whether
# the month times the day is equal to the year. If so, it should display
# a message saying the date is magic. Otherwise, it should display a
# message saying the date is not magic. 6/10/60!

month = int(input("Please enter a month (in numeric form): "))
day = int(input("Please enter a day (in numeric form): "))
year = int(input("Please enter a two digit year (in numeric form): "))

magic_test = month * day

if magic_test != year:
    print("The date is not magic.")
else:
    print("The date is magic!")