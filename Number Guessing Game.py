# number-guessing-game.py

import random

def main():
    # Initialize counters for high, low, and win
    high = 0
    low = 0
    win = 0

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    while win == 0:
        # Ask the user to input a guess
        userNum = int(input("Please guess a number between 1 and 100: "))

        # Check if the user's guess is too high, correct, or too low
        if userNum > number:
            message = "Too high, try again."
            high += 1
        elif userNum == number:
            message = "You got it correct! Congratulations!"
            win += 1
        else:
            message = "Too low, try again."
            low += 1

        # Print the appropriate message
        print()
        print(message)

    # Display the total number of guesses
    print()
    print("Number of times too high:", high)
    print("Number of times too low:", low)
    print("Total number of guesses:", high + low + win)

# Call the main function to start the game
main()