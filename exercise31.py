import random
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
        print("incorrect!")
print(f"The word was: {word}")
