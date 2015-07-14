# Rock paper scissors game

# Define functions

def player_one_choice():
    """Get rock, paper or scissors from p1, and return choice as number 1 through 3"""
    choice = input("Player 1: Please enter either (R)ock, (P)aper, or (S)cissors: ").lower()

    if choice == "r":
        return 1

    elif choice == "p":
        return 2

    elif choice == "s":
        return 3

def player_two_choice():
    """Get rock, paper or scissors from p2, and return choice as a number 1 through 3"""
    choice = input("Player 2: Please enter either (R)ock, (P)aper, or (S)cissors: ").lower()

    if choice == "r":
        return 1

    elif choice == "p":
        return 2

    elif choice == "s":
        return 3

def determine_winner(player_one, player_two):
    """ Compare choices between players, calculate winner and return result"""
    # Return 1 if player one wins, 2 if player two wins, and 0 for a tie
    if player_one == 1 and player_two == 3:
        return 1

    elif player_one == 1 and player_two == 2:
        return 2

    elif player_one == 2 and player_two == 3:
        return 2

    elif player_one == 2 and player_two == 1:
        return 1

    elif player_one == 3 and player_two == 2:
        return 1

    elif player_one == 3 and player_two == 1:
        return 2
    else:
        return 0

def print_results(winner):
    """Take returned value from determineWinner function and display result"""
    if winner == 1:
        print("Player 1 wins.")
    elif winner == 2:
        print("Player 2 wins.")
    elif winner == 0:
        print("There was a tie.")

# Play game

player_one = player_one_choice()    
player_two = player_two_choice()    
winner = determine_winner(player_one, player_two)   
results = print_results(winner)
