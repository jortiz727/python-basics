#Create a list of words and randomly select one.
#Display blanks (_) for each letter in the word.
#Take a letter as input from the user.
#Check whether the letter exists in the word.
#Reveal correct letters and track wrong guesses.
#Display the Hangman drawing after each incorrect guess.
#End the game when the word is guessed or all chances are used.

import random
from pathlib import Path
WORDS_FILE = Path(__file__).parent / "words.txt"

with open(WORDS_FILE) as file:
    text = file.read()

words = []
for word in text.split():
    if 5 <= len(word) <= 8 and word.isalpha():
        words.append(word.lower())

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
        """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")

while wrong_guesses < max_attempts:

    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        print("The Word was:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The Word was:", secret_word)