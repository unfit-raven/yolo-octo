def count(paragraph):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    number_of_e = 0
    total_char = 0
    for achar in paragraph:
        if achar in lower or achar in upper:
            total_char = total_char + 1
            if achar == "e":
                number_of_e = number_of_e + 1

    percent_With_e = (number_of_e/total_char) * 100
    print("Your text contains", total_char, "alphabetic characters of which", number_of_e, "(", percent_with_e, "%)", "are e.")

    paragraph = '''
    "If the automobile had followed the same development cycle as the computer, a
    Rolls-Royce would today cost $100, get a million miles per gallon, and explode
    once a year, killing everyone inside."
    -Robert Cringely
    '''

    count(paragraph)
