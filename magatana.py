import os
import time
import random

# Lettres ASCII homogènes pour MAGATANA (5 lignes)
letters = {
    "A": [
        "    /\\    ",
        "   /  \\   ",
        "  /----\\  ",
        " /      \\ ",
        "/        \\"
    ],
    "G": [
        "  ____  ",
        " / ___| ",
        "| |  _  ",
        "| |_| | ",
        " \\____| "
    ],
    "M": [
        " __  __ ",
        "|  \\/  |",
        "| |\\/| |",
        "| |  | |",
        "|_|  |_|"
    ],
    "T": [
        " ______ ",
        "|_   _|",
        "  | |  ",
        "  | |  ",
        "  |_|  "
    ],
    "N": [
        " _   _ ",
        "| \\ | |",
        "|  \\| |",
        "| . ` |",
        "|_|\\__|"
    ]
}

word = "MAGATANA"

# Liste de couleurs ANSI néon
colors = [
    "\033[91m",  # rouge
    "\033[92m",  # vert
    "\033[93m",  # jaune
    "\033[94m",  # bleu
    "\033[95m",  # magenta
    "\033[96m",  # cyan
    "\033[97m"   # blanc
]

RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_word(current_letters):
    lines = [""] * 5
    for letter in current_letters:
        color = random.choice(colors)  # couleur aléatoire pour chaque lettre
        for i in range(5):
            lines[i] += f"{color}{letters[letter][i]}{RESET}  "
    print("\n".join(lines))

def animate_word(word, delay=0.3):
    while True:
        # Apparition progressive
        current = ""
        for l in word:
            current += l
            clear()
            print_word(current)
            time.sleep(delay)

        # Disparition progressive
        for i in range(len(word), 0, -1):
            clear()
            print_word(word[:i-1])
            time.sleep(delay)

# Lancer l'animation
animate_word(word)
