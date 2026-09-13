import random
x = random.randint(1, 9)
counter = 0
y = input("Pick a number between 1 and 9 (or exit): ")
while y != "exit":
    try:
        y = int(y)
    except ValueError:
        print("This is not an integer!")
        y = input("Try again! Pick a number between 1 and 9 (or exit): ")
        continue
    if y < 1 or y > 9:
        y = input("Try again! Pick a number between 1 and 9 (or exit): ")
    else:
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
    print(f"You made {counter} guesses before exiting.")