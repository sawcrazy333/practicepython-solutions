def horizontal(n):
    return " " + "--- " * n
def vertical(n):
    return "|   " * n + "|"
def board(size):
    for i in range(size * 2 + 1):
        if i % 2 == 0:
            print(horizontal(size))
        else:
            print(vertical(size))
