"""Structured Wordle with multiple guesses."""

__author__ = "730579449"


def contains_char(length_infinite: str, one_character: str) -> bool:
    """Searches for second parameter that must be a singlr character."""
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


def emojified(length_infinite: str, secret_word: str) -> str:
    """If first a guess and second a secret it will return a string of emoji."""
    assert len(length_infinite) == len(secret_word)
    index: int = 0
    boxes: str = ""
    one_character = length_infinite[index]
    contains_char(length_infinite, one_character)
    while index < len(length_infinite):
        if length_infinite[index] == secret_word[index]:
            boxes += GREEN_BOX
        elif contains_char(secret_word, length_infinite[index]):
            boxes += YELLOW_BOX
        else: 
            boxes += WHITE_BOX
        index += 1
    return boxes


def input_guess(expected_length: int) -> str:
    """Prompt user for continious guesses."""
    length_infinite: str = input(f"Enter a {expected_length} character word: ")
    while len(length_infinite) != expected_length: 
        length_infinite = input(f"That wasn't {expected_length} chars! Try again: ")
    return length_infinite


def main() -> None:
    """Establishes secret word as a variable."""
    user_turns: int = 1
    secret_word: str = "codes"
    winner: bool = True
    while user_turns <= 6 and winner is True:
        print(f"=== Turn {user_turns}/6 === ") 
        length_infinite = input_guess(len(secret_word))
        print(emojified(length_infinite, secret_word))
        if length_infinite == secret_word:
            print(f"You won in {user_turns}/6 turns.")
            winner = False
        else: 
            user_turns += 1
    if winner is True:
        print("X/6 - Sorry, try again tomorrow!")
        
               
if __name__ == "__main__":
    main()