import random

# ---------------------------
# 1. WORD LIST (WITH HINTS)
# ---------------------------
words = {
    "python": "A popular programming language.",
    "internet": "A global network connecting computers.",
    "compiler": "Translates source code into machine code.",
    "database": "Stores and manages data.",
    "algorithm": "Step-by-step instructions to solve a problem."
}

# ---------------------------
# 2. HANGMAN VISUAL FIGURES
# ---------------------------
HANGMAN_PICS = [
    """
       -----
       |   |
           |
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
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# ---------------------------
# FUNCTION: PLAY ONE GAME
# ---------------------------
def play_game():
    # Step 1: Select random word + hint
    word, hint = random.choice(list(words.items()))

    # Step 2: Game Setup
    guessed = ["_"] * len(word)
    used_letters = []
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("\nWelcome to HANGMAN!")
    print(f"Hint: {hint}")

    # ---------------------------
    # 3. GAME LOOP
    # ---------------------------
    while attempts < max_attempts:

        # Step 3: Display Interface
        print(HANGMAN_PICS[attempts])
        print("Word:", " ".join(guessed))
        print("Used letters:", ", ".join(used_letters))

        # Step 4: User Input Validation
        letter = input("Guess a letter: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if letter in used_letters:
            print("You already guessed this letter.")
            continue
        
        used_letters.append(letter)

        # Step 5: Check Guess
        if letter in word:
            print("Correct guess!")
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
        else:
            print("Wrong guess!")
            attempts += 1

        # Step 6: Win Condition
        if "_" not in guessed:
            print(HANGMAN_PICS[attempts])
            print("Word:", " ".join(guessed))
            print("\nYou Win! The word was:", word)
            return

    # Step 7: Loss Condition (loop ended)
    print(HANGMAN_PICS[-1])
    print("\nGame Over! The correct word was:", word)

# ---------------------------
# MAIN LOOP: PLAY AGAIN OPTION
# ---------------------------
while True:
    play_game()  

    choice = input("\nWould you like to play again? (yes/no): ").lower()
    if choice not in ["yes", "y"]:
        print("Thanks for playing Hangman!")
        break