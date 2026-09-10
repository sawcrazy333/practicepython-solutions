import random
def random_word(txt):
    with open(txt, 'r') as file:
        lines = [line.strip() for line in file]
    return random.choice(lines)
word = random_word('SOWPODS.txt')
print(word)