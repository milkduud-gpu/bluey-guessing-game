import argparse
import os
import random
import sys

WORDS = [
    "python", "hangman", "computer", "keyboard", "program", "variable",
    "function", "network", "monitor", "software", "algorithm", "database",
    "internet", "terminal", "developer", "compile", "library", "package",
]

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

BANNER = f"""{MAGENTA}{BOLD}
  ╔═══════════════════════════════════╗
  ║  {YELLOW}★{CYAN} H A N G M A N   P A R T Y {YELLOW}★{MAGENTA}  ║
  ╚═══════════════════════════════════╝{RESET}"""

FACES = ["", "(^o^)", "(o_o)", "(O_O)", "(>_<)", "(;_;)", "(x_x)"]
MAX_WRONG = len(FACES) - 1


def draw(wrong):
    head = FACES[wrong] if wrong >= 1 else "     "
    arms_l = "\\" if wrong >= 3 else " "
    arms_r = "/" if wrong >= 4 else " "
    body = "|" if wrong >= 2 else " "
    leg_l = "/" if wrong >= 5 else " "
    leg_r = "\\" if wrong >= 6 else " "
    color = [GREEN, GREEN, YELLOW, YELLOW, RED, RED, RED][wrong]
    return (
        f"{BLUE}   ┏━━━━━┓\n"
        f"   ┃     ┃\n"
        f"   ┃{color}  {head}{BLUE}\n"
        f"   ┃{color}   {arms_l}{body}{arms_r}{BLUE}\n"
        f"   ┃{color}   {leg_l} {leg_r}{BLUE}\n"
        f" ━━┻━━━━━━━━{RESET}"
    )


def hearts(wrong):
    left = MAX_WRONG - wrong
    return "❤️ " * left + "🖤 " * wrong


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def screen(word, guessed, wrong, message=""):
    clear()
    print(BANNER)
    print(draw(wrong))
    shown = " ".join(
        f"{CYAN}{BOLD}{c.upper()}{RESET}" if c in guessed else f"{YELLOW}_{RESET}"
        for c in word
    )
    print(f"\n  🔤  {shown}")
    bad = " ".join(sorted(g for g in guessed if g not in word))
    print(f"  ❌  {RED}{bad or '-'}{RESET}")
    print(f"  Lives: {hearts(wrong)}")
    if message:
        print(f"\n  {message}")


def load_words(path):
    with open(path) as f:
        words = [w.strip().lower() for w in f]
    words = [w for w in words if w.isalpha()]
    if not words:
        sys.exit(f"No usable words found in {path} (one alphabetic word per line).")
    return words


def play(words):
    word = random.choice(words)
    guessed = set()
    wrong = 0
    message = f"{MAGENTA}Can you save my little buddy? 🎈{RESET}"

    while True:
        screen(word, guessed, wrong, message)

        if all(c in guessed for c in word):
            print(f"\n  🎉🎉 {GREEN}{BOLD}YOU WIN! Hooray!{RESET} 🎉🎉")
            return
        if wrong >= MAX_WRONG:
            print(f"\n  💀 {RED}{BOLD}Oh no! The word was '{word}'.{RESET} 💀")
            return

        guess = input(f"\n  {BOLD}Guess a letter ➜ {RESET}").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            message = f"{YELLOW}🤔 One letter at a time, please!{RESET}"
        elif guess in guessed:
            message = f"{YELLOW}🔁 You already tried '{guess}'!{RESET}"
        else:
            guessed.add(guess)
            if guess in word:
                message = f"{GREEN}✨ Nice! '{guess}' is in the word!{RESET}"
            else:
                wrong += 1
                message = f"{RED}💥 Oops! No '{guess}' here!{RESET}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play hangman against the computer.")
    parser.add_argument("-w", "--words", metavar="FILE",
                        help="text file with one word per line (default: built-in list)")
    args = parser.parse_args()
    try:
        words = load_words(args.words) if args.words else WORDS
    except OSError as e:
        sys.exit(f"Could not read word list: {e}")
    try:
        while True:
            play(words)
            if input("\n  Play again? (y/n) ➜ ").strip().lower() != "y":
                break
        print(f"\n  {CYAN}Thanks for playing! 👋{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n  {CYAN}Goodbye! 👋{RESET}")
