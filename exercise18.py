import random

def generate_number():
    return [random.randint(0, 9) for _ in range(4)]

def count_cows_bulls(guess, answer):
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == answer[i]:
            cows += 1
        elif guess[i] in answer:
            bulls += 1
    return cows, bulls

def main():
    answer = generate_number()
    print("Welcome to the Cows and Bulls Game!")

    tries = 0
    while True:
        guess = [int(n) for n in input("Guess a 4 digit number: ")]
        if len(guess) != 4:
            print("Please enter a 4 digit number")
            continue
        tries += 1
        if guess == answer:
            answer_str = "".join(str(n) for n in answer)
            print(f"Congratulations! You guessed it: {answer_str}")
            print(f"It took you {tries} tries!")
            break
        cows, bulls = count_cows_bulls(guess, answer)
        print(f"Cows: {cows}, Bulls: {bulls}")

if __name__ == "__main__":
    main()