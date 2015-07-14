# Robert McKinney
# Week Six Assignment Part 2

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


def all_num_avg(numlist):
    """Take a list of all numbers and calculate the average, then return average"""
    total_sum = 0  # Create empty variable to hold sum
    total_count = 0  # Create empty variable to hold count
    for num in numlist:  # Iterate through each number in the list
        total_sum += num  # Add each number to the sum variable
        total_count += 1  # Add one to count variable each loop
    total_average = total_sum/total_count  # Calculate average

    return total_average  # Return calculated average


def pos_num_avg(numlist):  # Follows the same structure as "all_num_avg" function
    """Take a list of positive numbers and calculate the average, then return average"""
    pos_sum = 0
    pos_num_count = 0
    for num in numlist:
        pos_sum += num
        pos_num_count += 1
    pos_average = pos_sum/pos_num_count

    return pos_average


def non_pos_avg(numlist):  # Follows the same structure as "all_num_avg" function
    """Take a list of negative numbers and calculate the average, then return average"""
    non_pos_sum = 0
    non_pos_num_count = 0
    for num in numlist:
        non_pos_sum += num
        non_pos_num_count += 1
    non_pos_average = non_pos_sum/non_pos_num_count

    return non_pos_average


def average_dictionary(total, pos_total, neg_total):
    """Take returned averages as parameters and create dictionary with those values"""
    avg_dictionary = {'AvgAllNum': total, 'AvgPositive': pos_total, 'AvgNonPos': neg_total}

    return avg_dictionary


# Call all_num_avg function and pass all_num as parameter, saving returned value in variable
total_average = all_num_avg(all_num)

# Call pos_num_avg function and pass all_pos_num as parameter, saving returned value in variable
pos_average = pos_num_avg(all_pos_num)

# Call non_pos_avg function and pass all_non_pos_num as parameter, saving returned value in variable
non_pos_average = non_pos_avg(all_non_pos_num)

# Print the list containing all numbers
print("The list of all numbers entered is: ", '\n', all_num)

# Call the average_dictionary function and pass three parameters, printing the returned item
print("The dictionary with averages is: ", '\n',
      average_dictionary(total_average, pos_average, non_pos_average))