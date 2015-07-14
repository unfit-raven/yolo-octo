# Write a program that asks the user for a number of seconds, and
# then calculates the number of minutes, hours or days in that
# many seconds.

seconds = eval(input("Please enter a number of seconds: "))

if seconds < 60:
    print("That's less than one minute.")
elif seconds >= 60 and seconds < 3600:
    minutes = seconds / 60
    print(minutes, "minutes are in", seconds, "seconds.")
elif seconds >= 3600 and seconds < 86400:
    hours = seconds / 3600
    print(hours, "hours are in", seconds, "seconds.")
elif seconds >= 86400:
    days = seconds / 86400
    print(days, "days are in", seconds, "seconds.")


