# Exercise 1: Working with a while loop
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1,10)
print(f"spoiler: the number is {number}")

isGuessRight = False

while not isGuessRight:
    guess = input("Guess a number between 1 and 10: ")
    print(f"You guessed {guess}. ", end = "")
    if int(guess) == number:
        print("That is correct! You win!")
        isGuessRight = True
    else:
        print("Sorry, that isn’t it. Try again.")