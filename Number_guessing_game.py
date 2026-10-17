
import random

secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < 1 or guess > 20:
        print("Choose a number between 1 and 20.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You won!")
        print("Attempts:", attempts)
        break
