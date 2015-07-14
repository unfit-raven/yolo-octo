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

