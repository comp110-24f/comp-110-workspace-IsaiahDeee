"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730583303"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    while True:
        guess_word = input("Enter a 5-character word: ")
        if len(guess_word) == 5:
            return guess_word
        else:
            print("Error: word must contain 5 characters.")
            exit()
            return guess_word


def input_letter() -> str:
    while True:
        guess_letter = input("Enter a single character: ")
        if len(guess_letter) == 1:
            return guess_letter
        else:
            print("Error: Character must be a single character.")
            exit()
    return guess_letter


def contains_char(word: str, letter: str) -> None:
    instances: int = 0
    if len(letter) != 1:
        print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        instances = instances + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        instances = instances + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        instances = instances + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        instances = instances + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        instances = instances + 1
    if instances == 0:
        print("No instances of " + letter + " in " + word)
    else:
        print(str(instances) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
