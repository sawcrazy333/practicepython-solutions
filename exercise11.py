def isPrime(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return len(divisors) == 2
number = int(input("Enter a number: "))
if isPrime(number):
    print("It's a prime number!")
else:
    print("It's not a prime number!")