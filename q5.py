# q5.py
# Problem: Functions and While Loop - Number Guessing Game
# Write a Python script that implements a simple number guessing game.
# The script should:
# 1. Generate a random number between 1 and 100 (inclusive).
# 2. Use a function that takes the user's guess as input.
# 3. Use a while loop to allow the user to keep guessing until they guess correctly.
# 4. Provide feedback to the user if their guess is too high or too low.
# 5. Count the number of attempts and display it when the user guesses correctly.

import random # Module to generate random numbers

def guessing_game():
    """
    Implements a number guessing game.
    """
    print("--- Number Guessing Game (1-100) ---")

    # 1. Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("I've picked a number between 1 and 100. Try to guess it!")

    # 3. Use a while loop for guessing
    while not guessed_correctly:
        try:
            # 2. Get user's guess (handled inside the loop for repeated guesses)
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)
            attempts += 1

            # 4. Provide feedback
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else: # Guess is correct
                guessed_correctly = True
                # 5. Display result
                print(f"Congratulations! You guessed the number {secret_number} correctly.")
                print(f"It took you {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break # Exit loop on unexpected error

if __name__ == "__main__":
    guessing_game()

# How to test:
# - Run the script.
# - Try guessing numbers.
# - Observe "Too low" / "Too high" feedback.
# - Test inputting non-numbers (e.g., "abc") to see error handling.
# - Test numbers outside the 1-100 range.
# - Eventually, guess the correct number and check the attempt count.
