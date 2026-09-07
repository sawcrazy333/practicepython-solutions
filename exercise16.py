import random
import string

def weak_password():
    length = random.randint(3, 5)
    password = [random.choice(string.digits) for _ in range(length)]
    return "".join(password)

def mid_password():
    length = random.randint(8, 11)
    znaki = string.digits + string.ascii_lowercase + string.ascii_uppercase
    password = [random.choice(znaki) for _ in range(length)]
    return "".join(password)

def strong_password():
    length = 15
    znaki = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password = [random.choice(znaki) for _ in range(length)]
    return "".join(password)

def main():
        print("1 - Weak password")
        print("2 - Mid password")
        print("3 - Strong password")
        while True:
            choice = input("Choose option (1-3): ")

            if choice == "1":
                print(weak_password())
            elif choice == "2":
                print(mid_password())
            elif choice == "3":
                print(strong_password())
            else:
                print("Incorrect choice, try again.")

main()