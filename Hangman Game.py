import random

# Step 1: Predefined list of 5 words
word_list = ["apple", "chair", "water", "phone", "light"]

# Step 2: Choose one word randomly from the list
secret_word = random.choice(word_list)

# Step 3: Set up variables
guessed_letters = []
max_attempts = 6
wrong_guesses = 0

# Step 4: Create a function to show the current progress
def display_word():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Step 5: Game Loopa

print(" Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} incorrect guesses allowed.\n")

while wrong_guesses < max_attempts:
    print("Word:", display_word())
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_attempts - wrong_guesses} attempts left.\n")

    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("💀 Game Over! The word was:", secret_word)
