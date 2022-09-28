"""one shot wordle."""

__author__ = "730579449"

correct_word: str = "python"
word_number = len(correct_word)
typed_word: str = input(f"What is your {word_number}-letter guess? ")
i: int = 0
index: int = 0
answer: str = ""

YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"

while len(typed_word) != word_number:
    typed_word = input(f"That was not {word_number} letters! Try again: ")

if len(typed_word) == len(correct_word) and typed_word != correct_word:
    while i < word_number:
        index = 0
        correct_char: bool = False
        if typed_word[i] == correct_word[i]:
            answer += GREEN_BOX 
        if typed_word[i] != correct_word[i]:
            while correct_char is not True and index < len(typed_word):
                if correct_word[index] == typed_word[i]:
                    correct_char = True
                index += 1 
            if correct_char is not True:
                answer += WHITE_BOX
            else:
                answer += YELLOW_BOX
        i += 1 
    print(answer)
    print("Not quite. Play again soon!")

if typed_word == correct_word:
    print("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")
    print("Woo! You got it!")