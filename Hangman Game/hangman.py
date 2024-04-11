import random


def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi"]
    return random.choice(words)


def hangman():
    word = choose_word()
    guessed = "_" * len(word)
    attempts = 6
    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        letter = input("Guess a letter: ").lower()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed = guessed[:i] + letter + guessed[i+1:]
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")


hangman()
