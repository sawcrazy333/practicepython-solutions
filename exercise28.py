def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
print(f"The largest number is {find_largest(a, b, c)}")