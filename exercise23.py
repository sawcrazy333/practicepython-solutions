def primeandhappy(file1, file2):
    f1_list = []
    f2_list = []
    with open(file1, 'r') as f1:
        for number1 in f1:
            f1_list.append(int(number1))
    with open(file2, 'r') as f2:
        for number2 in f2:
            f2_list.append(int(number2))
    f3_list = sorted(set(f1_list) & set(f2_list))
    return f3_list
overlap = primeandhappy('exercise22file1.txt', 'exercise22file2.txt')
print(overlap)