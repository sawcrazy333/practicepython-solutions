import random
a = [random.randint(1, 100) for _ in range(random.randint(10, 15))]
b = [random.randint(1, 100) for _ in range(random.randint(10, 15))]
c = [i for i in a if i in b]
print(a)
print(b)
print(list(set(c)))