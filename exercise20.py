def in_list(lst, number):
    return number in lst
print(in_list([1, 3, 5, 30, 42, 43, 500], 10))

def binary_search(a, number):
    while len(a) != 0:
        if (a[len(a) // 2]) == number:
            return True
        elif (a[len(a) // 2] > number):
            a = a[:len(a)//2]
        elif (a[len(a) // 2] < number):
            a = a[((len(a)//2)+1):]
    else: return False
print(binary_search([1, 3, 5, 30, 42, 43, 500], 10))