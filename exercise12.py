import random
a = [random.randint(1, 100) for i in range (random.randint(5, 10))]
print(a)
def new_list(a):
    x = a[0]
    y = a[-1]
    return [x,y]
print(new_list(a))