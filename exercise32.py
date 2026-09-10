import random

def hangman():
    def random_word(txt):
        with open(txt, 'r') as file:
            lines = [line.strip() for line in file]
        return random.choice(lines)
    word = random_word('SOWPODS.txt')

    guessed_letters = []
    word_characters = list(word)
    word_hidden = ["_" for _ in range(len(word_characters))]
    print("Welcome to Hangman!")
    print(word_hidden)
    bad_guesses = 0
    while word_hidden != word_characters:
        letter = input("guess a letter: ")
        if letter in guessed_letters:
            print("this letter was already guessed")
            continue
        guessed_letters.append(letter)
        if letter in word_characters:
            for i in range(len(word_characters)):
                if word_characters[i] == letter:
                    word_hidden[i] = letter
            print(word_hidden)
        else:
            bad_guesses += 1
            print(f"incorrect, you have {6 - bad_guesses} tries left!")
            if bad_guesses == 6:
                break
    if word_hidden == word_characters:
        print(f"You have won! The word was: {word}")
    else:
        print(f"You lost! The word was: {word}")

def play():
    while True:
        hangman()
        again = input("play again? (y/n): ").strip().lower()
        if again != "y":
            print("thanks for playing!")
            break
play()