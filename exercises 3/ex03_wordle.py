"""Structured Wordle with multiple guesses."""

__author__ = "730579449"

from pyexpat.errors import codes


def contains_char(length_infinite: str, one_character: str) -> bool:
    """Searches for second parameter that must be a singlr character"""
    assert len(one_character) == 1
    length_infinite_index: int = 0
    while length_infinite_index < len(length_infinite):
        if length_infinite[length_infinite_index] == one_character:
            return True
        else:
            length_infinite_index += 1
    return False

YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"

def emojified(guess_word: str, secret_word: str) -> str:
    """If first a guess and second a secret it will return a string of emoji"""
    assert len(guess_word) == len(secret_word)
    index: int = 0
    boxes: str = ""
    index = 0
    while index < len(guess_word):
        if guess_word[index] == secret_word[index]:
            boxes += GREEN_BOX
            index += 1
        elif contains_char(secret_word, guess_word[index]):
            boxes += YELLOW_BOX
            index += 1
        else: 
            boxes+= WHITE_BOX
            index+= 1

    return boxes

def input_guess(expected_length: int) -> str:
    """Prompt user for continious guesses"""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length: 
        user_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess

def main() -> None:
    """Establishes secret word as a variable."""
    user_turns: int = 1
    answer: str = "codes"
    winner: bool = False

    while user_turns <= 6 and winner is False:
        print(f"=== Turn {user_turns}/6 === ") 
        user_word = input_guess(len(answer))
        print(emojified(user_word, answer))

        if user_word == answer:
            winner = True
            print(f"You won in {user_turns} turns")
        else: 
            user_turns += 1
        
        if winner is False:
            print("X/6 - Sorry, try again tomorrow!")
        
               
if __name__ == "__main__":
    main()