import random
import math

## Use a for statement to print 10 random numbers.
for i in range(10):
    x = random.random()
    print(x)

        
## Blank line for space in Shell
print()


## change the program to multiply x * 5
for i in range(10):
    x = random.random()
    print(x*5)

    
## Blank line for space in Shell
print()


## Change the program to print 10 random numbers between 25 and 35
for i in range(10):
    x = random.randrange(25,36)
    print(x)

## Blank line for space in Shell
print()


## Create hypotenuse calculator
side1 = 5
side2 = 3

hypotenuse = math.hypot(side1,side2)
print(hypotenuse)

## Blank line for space in Shell
print()

## Pi approximator, and real Pi
approx1 = 256/81
approx2 = 25/8
approx3 = 339/108
approx4 = 223/71
approx5 = 3927/1250
pi = math.pi

print(approx1)
print(approx2)
print(approx3)
print(approx4)
print(approx5)

print("Real:", pi)
