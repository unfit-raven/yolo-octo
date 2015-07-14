# Robert McKinney
# Week 4 Assignment 4 Part 1


def partOneA():
    for i in range(10):
        for j in range(10):
            print(j, end=" ")
        print("\n")


def partOneB():
    for i in range(10):
        for j in range(10):
            print(i, end=" ")
        print("\n")


def partTwo():
    rangeValue = 0  ## Initialize to 0
    for i in range(10):
        rangeValue = rangeValue + 1  ## Increment by 1 each loop
        for j in range(rangeValue):
            print(j, end=" ")
        print("\n")


def extraCredit():
    rangeValue = 0  ## Initialize to 0
    x = 10  ## Initialize to 10 per sample run
    for i in range(9):  ## Run loop 9 times to end on 54 per sample run
        rangeValue = rangeValue + 1  ## Increment by 1 each loop
        for j in range(rangeValue):
            print(x, end=" ")
            x += 1  # Increment by 1 each loop
        print("\n")


partOneA()

# Blank line for space between homework parts
print()

partOneB()

# Blank line for space between homework parts
print()

partTwo()

# Blank line for space between homework parts
print()

extraCredit()
