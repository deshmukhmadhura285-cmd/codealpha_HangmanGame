import random

words = ["python", "apple", "banana", "school", "computer"]

word = random.choice(words)
guessed_letters = [ ]
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:
    display = " "

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)