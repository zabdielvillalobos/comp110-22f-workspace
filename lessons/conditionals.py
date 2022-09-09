""""An example of conditional with (if-else) statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = input("What is your guess? ")

if guess == SECRET: 
    print("You guessed correctly!!!")

print("Game over.")