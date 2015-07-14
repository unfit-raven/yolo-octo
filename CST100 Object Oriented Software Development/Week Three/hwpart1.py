# Robert McKinney
# Number game

import random                   # Import random module

number = random.randint(1, 20)  # Initialize variable with a random integer between 1 and 20
numAttempts = 0                 # Initialize counter 

# Get user's name
name = input("Hello! What's your name? ")
print("Well,", name + "," " I'm thinking of an integer between 1 and 20.")

# Main loop
while numAttempts < 3:
    guess = int(input("Take a guess. "))
    numAttempts = numAttempts + 1   ## Increment counter
    
    if guess < number:
        print("Your guess is too low." )
    if guess > number:
        print("Your guess is too high. ")
    if guess == number:
        break

if guess == number:
    print("Good job,", name + "! You guessed my number in", numAttempts, "guesses!")
if guess != number:
    print("Sorry, your three guesses are over. The number I was thinking of was", number)
