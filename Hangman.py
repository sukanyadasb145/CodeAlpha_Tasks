import random
words = ["adventure","elephant","umbrella","hospital","airplane"]
hangman = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]
word = random.choice(words)
display = ["_"] * len(word)

guessed_letters = []
wrong_guesses = 0

print("Welcome to Hangman")
while wrong_guesses < 6 and "_" in display:

    print(hangman[wrong_guesses])

    print("\nWord:", " ".join(display))
    print("Guessed Letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong")
        wrong_guesses += 1

if "_" not in display:
    print("You Won!")
    print("The word was:", word)

else:
    print(hangman[6])
    print("OOPS!!Better luck next time")
    print("The word was:", word)