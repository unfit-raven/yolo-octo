# Calculates the area of a trapezoid

# Get height of trapezoid from user
height = int(input("Enter the height of the trapezoid: "))

# Get length of bottom base from user
bottom_base = int(input("Enter the length of the bottom base: "))

# Get length of top base from user
top_base = int(input("Enter the length of the top base: "))

# Calculate area of trapezoid
area = 0.5 * (bottom_base + top_base) * height

# Print result to user
print("The area of the trapezoid is", area)

