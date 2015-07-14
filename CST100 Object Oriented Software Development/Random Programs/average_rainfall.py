# Write a program that uses nested loops to collect data and calculate
# the average rainfall over a period of years. First the program should
# ask for the number of years. The outer loop will iterate once per year.
# The inner loop will iterate 12 times, once per month. Each iteration
# of the inner loop will ask the user for the inches of rainfall for that
# month. After all iterations, the program should display the number of
# months, the total inches of rainfall, and the average rainfall per
# month for the entire period.

print("Average Rainfall Calculator")
number_of_years = int(input("Enter the number of years: "))

total_rainfall = 0
for each_year in range(number_of_years):
    for each_month in range(12):
        inches_of_rainfall = eval(input("Enter inches of rain for the month: "))
        total_rainfall += inches_of_rainfall

total_months = number_of_years * 12
average_rainfall = total_rainfall / total_months

print("The total number of months is", total_months, "and the average rainfall is", average_rainfall)