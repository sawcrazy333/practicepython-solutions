number = int(input("Enter a number: "))
if number%2 == 0 and number%4 == 0:
    print(number, "is multiple of 4")
elif number%2 == 0 and number%4 != 0:
    print(number, "is even")
else :
    print(number, "is odd")