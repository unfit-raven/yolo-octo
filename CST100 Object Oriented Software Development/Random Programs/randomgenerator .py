## Random generator until 2

import random

def main():

    rand = random.randint(1, 6)

    while rand != 2:
        print(rand)
        rand = random.randint(1, 6)
    else:
        print(rand)

main()
