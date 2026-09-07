counter = 0
number = 50
minimum = 0
maximum = 100
print(f"Is your number equal to {number}?")
answer = input()
while True:
    if answer == "too high":
        counter += 1
        maximum = number - 1
        number = (minimum + maximum) // 2
        print(f"Is your number equal to {number}?")
        answer = input()
    elif answer == "too low":
        counter += 1
        minimum = number + 1
        number = (minimum + maximum) // 2
        print(f"Is your number equal to {number}?")
        answer = input()
    elif answer == "right":
        counter += 1
        print(f"It took me {counter} guesses!")
        break
    else:
        print("only options are too high, too low or right")
        answer = input()