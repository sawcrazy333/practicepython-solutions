import random
x = random.randint(1, 9)
y = input("Pick a number between 1 and 9: ")
counter = 0
while y != "exit":
    y = int(y)
    counter += 1
    if x == y:
        print("Exactly right!")
        print(f"You needed {counter} tries!")
        break
    elif x > y:
        print("Too low!")
    else:
        print("Too high!")
    y = input("Try again or exit: ")
if y == "exit":
    print(f"You made {counter} guesses before exitting.")