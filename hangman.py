import random

WORDS = [
    "python", "hangman", "computer", "keyboard", "program", "variable",
    "function", "network", "monitor", "software", "algorithm", "database",
    "internet", "terminal", "developer", "compile", "library", "package",
]

STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

MAX_WRONG = len(STAGES) - 1


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    while True:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(STAGES[wrong])
        print(f"\nWord: {display}")
        print(f"Guessed: {' '.join(sorted(guessed)) or '-'}")

        if all(c in guessed for c in word):
            print("\nYou win!")
            return
        if wrong >= MAX_WRONG:
            print(f"\nYou lost. The word was '{word}'.")
            return

        guess = input("\nGuess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
        elif guess in guessed:
            print("You already guessed that.")
        else:
            guessed.add(guess)
            if guess not in word:
                wrong += 1
                print("Nope!")


if __name__ == "__main__":
    try:
        while True:
            play()
            if input("\nPlay again? (y/n): ").strip().lower() != "y":
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
