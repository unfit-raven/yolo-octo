# Robert McKinney
# Week Six Assignment Part 1


def find_longest_word(wordlist):
    """
    Function to take a list as a parameter, and return the longest
    item in the list
    """
    print("The list of words entered is:", '\n', wordlist)
    longest_word = ""    # Declare empty variable to hold longest word
    for word in wordlist:    # Iterate through each word in wordList parameter
        if len(word) > len(longest_word):  # Use len function and if statement for comparison
            longest_word = word  # Assign longest iterated word to previously declared variable
    return longest_word

# Get user input
user_input = input('Please enter a few words separated by a space, and I will '
                   'find the longest: ')

# Use split function to separate string from user into a list
words = user_input.split()

# Call function, pass the list, and assign returned value to variable
final_word = find_longest_word(words)

# Display longest word to user
print("The longest word in the list is:", '\n', final_word)
