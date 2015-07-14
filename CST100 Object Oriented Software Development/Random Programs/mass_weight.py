# Write a program that asks the user to enter an object's mass,
# and then calculate its weight. If the object weighs more than
# 1000 Newtons, display a message indicating that it is too
# heavy. Of the object weighs less than 10 Newtons, display a
# message indicating that the object is too light.
# Newtons -> weight = mass x 9.8

mass = eval(input("Please enter an object's mass: "))

weight = mass * 9.8

if weight > 1000:
    print("The weight of the object is", weight, "The object is too heavy.")
elif weight < 10:
    print("The weight of the object is", weight, "The object is too light.")
else:
    print("The weight of the object is", weight, "The object's weight is OK.")
