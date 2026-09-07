game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]
def check_winner(game):
    first_row = game[0]
    second_row = game[1]
    third_row = game[2]
    first_column = [wiersz[0] for wiersz in game]
    second_column = [wiersz[1] for wiersz in game]
    third_column = [wiersz[2] for wiersz in game]
    diagonal_down = [first_row[0], second_row[1], third_row[2]]
    diagonal_up = [third_row[0], second_row[1], first_row[2]]
    if first_row == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif second_row == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif third_row == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif first_column == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif second_column == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif third_column == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif diagonal_up == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif diagonal_down == [1, 1, 1]:
        print("the winner is 1")
        return 1
    elif first_row == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif second_row == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif third_row == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif first_column == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif second_column == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif third_column == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif diagonal_up == [2, 2, 2]:
        print("the winner is 2")
        return 2
    elif diagonal_down == [2, 2, 2]:
        print("the winner is 2")
        return 2
    else:
        print("draw")
        return 0
check_winner(game)