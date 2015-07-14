# Distance traveled calculator.
# Distance = Speed * Time

# Input validation - positive number for speed, and number greater than 1 for time.
speed = 0  # Priming read
while speed <= 0:
    speed = eval(input("Please enter the speed of the vehicle in MPH: "))
    if speed > 0:  # Speed validation
        print("Error. Try again.")
    else:
        print("Unknown error. Try again.")
time = 0  # Priming read
while time < 1:
    time = eval(input("Please enter the time traveled in hours: "))
    if time < 1:  # Time validation
        print("Error. Try again.")
    else:
        print("Unknown error. Try again.")

# Calculate distance
distance = speed * time

# Display results
print("The speed of the vehicle was", speed, "MPH and the time traveled was", time,
      "hours. The total distance traveled was", distance, "miles.")