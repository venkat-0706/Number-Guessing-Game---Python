## Number Guessing Game in Python

### Project Objectives

This project aims to:

* Implement a classic number guessing game in Python.
* Practice fundamental programming concepts like random number generation, user input, conditional statements, and loops.
* Create a user-friendly and interactive experience.

### What I Learned

Developing this game helped me solidify my understanding of:

* The `random` module for generating random numbers.
* Working with user input and converting it to the desired data type (integer in this case).
* Utilizing conditional statements (`if`, `elif`, `else`) for decision making.
* Implementing loops (`while`) for repetitive tasks.
* Displaying formatted output using `print` statements.

### Project Purpose

This number guessing game serves as a:

* **Learning tool:** It reinforces core Python programming concepts in a practical and engaging way.
* **Simple entertainment:** It provides a casual game experience for users to test their luck and intuition.

### How it Works

1. The program imports the `random` module.
2. It defines a function `main()` to encapsulate the game logic.
3. Inside `main()`:
    * Counters are initialized for high guesses, low guesses, and wins.
    * A random number between 1 and 100 is generated and stored.
    * A `while` loop continues until the player guesses correctly.
        * Inside the loop, the user is prompted to enter a guess.
        * The guess is compared to the secret number.
        * Based on the comparison (too high, too low, or correct), appropriate messages are displayed, and counters are updated.
    * After the loop, the total number of high, low, and overall guesses is displayed.
4. The `main` function is called to start the game.

### Efficiency

This implementation prioritizes readability and understanding over optimization. While the code is efficient for a simple game, more complex projects might require techniques to improve performance for larger data sets or frequent calculations. 

### Further Development

* Difficulty levels with adjustable number ranges.
* Limited number of attempts to add an element of challenge.
* Score tracking based on the number of guesses.

