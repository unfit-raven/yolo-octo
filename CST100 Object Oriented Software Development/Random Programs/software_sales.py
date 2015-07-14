# Write a program that asks the user to enter the number of
# software packages purchased. The program should then display
# the amount of the discount (if any) and the total amount of
# the purchase after the discount. Price of software is $99.
# 10-19 20%, 20-49 30%, 50-99 40%, 100+ 50%

purchase = eval(input("Please enter the number of software packages purchased: "))
price = 99
total = purchase * price

if purchase < 10:
    print("There is no discount for this amount. The total price is", total)
elif 10 <= purchase < 20:
    print("The discount for this amount is", total * .2, "The total price is", total - (total * .2))
elif purchase >= 20 and purchase < 50:
    print("The discount for this amount is", total * .3, "The total price is", total - (total * .3))
elif purchase >= 50 and purchase < 100:
    print("The discount for this amount is", total * .4, "The total price is", total - (total * .4))
elif purchase >= 100:
    print("The discount for this amount is", total * .5, "The total price is", total - (total * .5))