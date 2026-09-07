a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for number in a:
    if number < 5:
        b.append(number)
print(b)
print("////")
num = int(input("Enter a number: "))
for number in a:
    if number < num:
        c.append(number)
print(c)
