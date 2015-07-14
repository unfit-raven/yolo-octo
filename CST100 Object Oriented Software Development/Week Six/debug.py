all_num = []  # Create empty list for all numbers
all_pos_num = []  # Create empty list for all positive numbers
all_non_pos_num = []  # Create empty list for all negative numbers

# Get number from user
number = eval(input("Enter a number (-9999 to quit): "))  # Priming read, outside of loop
while number != -9999:  # -9999 is the sentinel to stop loop
    all_num.append(number)  # Insert all numbers into all_num list
    if number > 0:
        all_pos_num.append(number)  # Insert all positive numbers into all_pos_num list
    elif number <= 0:
        all_non_pos_num.append(number)  # Insert all non-positive numbers into all_non_pos_num list
    number = eval(input("Enter a number (-9999 to quit): "))  # Ask user to enter another number

def allNumAvg(numList):
    """Take a list of all numbers and calculate the average, then return average"""
    total_sum = 0
    total_count = 0
    for num in numList:
        total_sum += num
        total_count += 1
    total_average = total_sum/total_count

    return total_average

# Call all_num_avg function and pass all_num as parameter, saving returned value in variable
total_average = allNumAvg(all_num)

print(total_average)