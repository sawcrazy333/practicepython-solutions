def fibo(n):
    f = []
    a = 0
    b = 1
    for i in range(n):
        f.append(a)
        temp = a + b
        a = b
        b = temp
    return f
n = int(input("Enter a number: "))
print(fibo(n))