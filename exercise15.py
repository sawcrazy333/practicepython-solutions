s = input("Enter a string: ")
def reverse(s):
    reversed_list = []
    temp = list(s.split())
    for i in range(len(temp) - 1, -1, -1):
        reversed_list.append(temp[i])
    return reversed_list
print(" ".join(reverse(s)))
