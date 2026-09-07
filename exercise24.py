def horizontal(n):
    return n * (" --- ")
def vertical(n):
    return (n+1) * "|    "
def board(n):
    return n * (horizontal(n) + "\n" + vertical(n) + "\n") + horizontal(n)
print(board(int(input("please enter a board size: "))))