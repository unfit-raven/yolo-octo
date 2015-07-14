# A little deeper into objects and classes.


class Fraction:

    def __init__(self, top, bottom):

        self.num = top     # The numerator is on top
        self.den = bottom  # The denominator is on bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n

        return n

print(gcd(12, 16))

my_fraction = Fraction(3, 4)
print(my_fraction)

print(my_fraction.get_num())
print(my_fraction.get_den())
