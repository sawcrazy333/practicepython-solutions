game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
turns = 0
while turns < 9:
    if turns % 2 == 0:
        user_input = input("player 1 chooses where to place x (row, column): ").strip()
        coords = user_input.split(",")
        row = int(coords[0]) - 1
        col = int(coords[1]) - 1
        if game[row][col] == 0:
            game[row][col] = "x"
            turns += 1
            for row in game:
                print(row)
        else:
            print("this coordinate is already taken!")

    else:
        user_input = input("player 2 chooses where to place o (row, column): ").strip()
        coords = user_input.split(",")
        row = int(coords[0]) - 1
        col = int(coords[1]) - 1
        if game[row][col] == 0:
            game[row][col] = "o"
            turns += 1
            for row in game:
                print(row)
        else:
            print("this coordinate is already taken!")
