# Personal info program

name = "Robert McKinney"
address = "2116 E. Donner Dr., Tempe AZ 85282"
phone = "480 213 2197"
major = "Informnation Technology"

print(name)
print(address)
print(phone)
print(major)

print() # Blank line for space

# Sales prediction program

sales_division = 0.62
total_sales = 4600000

# Calculate amount sales division generated of total sales
amount = sales_division * total_sales
print("The sales division generated", amount, "for the company.")

print() # Blank like for space

# Land calculation

acre = 43560
total_land = 389767

number_of_acres = total_land / acre

print("The total number of acres is", number_of_acres)

print() # Blank like for space

# Restaurant bill calculator

# Get cost of meal
meal_price = float(input("What was the cost of the meal? "))
tax = 0.08 # 8 percent
tip = 0.20 # Tip 20 percent
tax_amount = meal_price * tax
# Calculate cost of meal with tax
meal_with_tax = (meal_price + tax_amount)
# Calculate cost of tip with tax
tip_amount= (meal_with_tax * tip)
# Calculate total cost of meal
total_cost = meal_with_tax + tip_amount

print("The meal charge is", meal_price)
print("The tax amount is", tax_amount)
print("The cost of the meal with tax is", meal_with_tax)
print("The tip amount is", tip_amount)
print("The total bill is", total_cost)

print() # Blank line for space

# Stock commission program

shares = 600
percent_commission = .02
price_per_share = 21.77

# Calculate amount paid for stock alone (without commission)
price_for_stock = shares * price_per_share
# Calculate amount of commission
commission_amount = price_for_stock * percent_commission
# Calculate total amount paid (stock plus commission)
total_price = price_for_stock + commission_amount

# Print results
print("The amount paid for the stock was", price_for_stock)
print("The amount of the commission was", commission_amount)
print("The total amount paid was", total_price)

print() # Blank line for space

# Energy drink comsumption

customers = 12467 # Number of customers surveyed
percent_purchase_energy_drinks = 0.14 # percentage of customers surveyed who purchase energy drinks
percent_prefer_citrus_flavor = 0.64 # percentage of those who purchased and prefer citrus flavor
# Calculate number of customers who purchase energy drinks
customers_purchase = customers * percent_purchase_energy_drinks
#Calculate number of customers who prefer citrus flavor
customers_citrus_flavor = customers_purchase * percent_prefer_citrus_flavor
# Display results
print(customers, "customers were surveyed.")
print(customers_purchase, "many of customers surveyed purchase energy drinks.")
print("Of those,", customers_citrus_flavor, "prefer a citrus flavor.")







