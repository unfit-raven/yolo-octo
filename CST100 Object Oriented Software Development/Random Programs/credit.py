# Available credit - program will calculate the amount of
# available credit a customer has.

# Get maximum amount of credit available to customer
maximum = int(input("Please enter the maximum amount of credit available to you: "))
# Get amount of credit used by customer
used = int(input("Please enter the amount of credit you have used: "))

# Calculate the amount of credit available
available = maximum - used

# Print results to user
print("You have", available, "dollars of credit available.")


print() # Blank line

# Sales tax program
# Calculates sales tax of of a purchase, and total price

# Get retail price item
retail_price = float(input("Please enter the retail price of the item: "))
# Get sales tax percentage as a decimal
tax_percentage = float(input("Please enter the sales tax percentage as a decimal: "))

# Calculate sales tax
sales_tax = retail_price * tax_percentage
# Calculate total cost of purchase
total_cost = retail_price + sales_tax

# Print results to user
print("The sales tax is", sales_tax, " dollars, and the total price is", total_cost, "dollars.")

