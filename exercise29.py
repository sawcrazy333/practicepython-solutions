def print_board(game):
    horizontal_line = " --- --- --- "
    for i, row in enumerate(game):
        cells = [str(cell) if cell != 0 else " " for cell in row]
        print(f"| {cells[0]} | {cells[1]} | {cells[2]} |")
        if i < len(game) - 1:
            print(horizontal_line)

def check_winner(game):
    first_row = game[0]
    second_row = game[1]
    third_row = game[2]
    first_column = [wiersz[0] for wiersz in game]
    second_column = [wiersz[1] for wiersz in game]
    third_column = [wiersz[2] for wiersz in game]
    diagonal_down = [first_row[0], second_row[1], third_row[2]]
    diagonal_up = [third_row[0], second_row[1], first_row[2]]
    if first_row == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif second_row == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif third_row == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif first_column == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif second_column == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif third_column == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif diagonal_up == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif diagonal_down == ["x", "x", "x"]:
        print("the winner is x")
        return "x"
    elif first_row == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif second_row == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif third_row == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif first_column == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif second_column == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif third_column == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif diagonal_up == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    elif diagonal_down == ["o", "o", "o"]:
        print("the winner is o")
        return "o"
    else:
        return 0

def coordinates(game):
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
                print_board(game)
                winner = check_winner(game)
                if winner != 0:
                    return
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
                print_board(game)
                winner = check_winner(game)
                if winner != 0:
                    return
            else:
                print("this coordinate is already taken!")
    print("draw")


def play():
    while True:
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        coordinates(game)

        again = input("play again? (y/n): ").strip().lower()
        if again != "y":
            print("thanks for playing!")
            break


play()