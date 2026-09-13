import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

with open("birthdays.json", "r") as file:
    names_dictionary = json.load(file)

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in names_dictionary:
    print(name)
name = input("Who's birthday do you want to look up? ")
if name in names_dictionary:
    print(f"{name}'s birthday is {names_dictionary[name]}")
else:
    print(f"{name} is not in the dictionary")

add_info = input("Do you want to add info about another scientist? (y/n) ")

if add_info == "y":
    new_name = input("Enter the new scientist's name: ")
    new_birthday = input("Enter new scientist's birthday: ")

    names_dictionary[new_name] = new_birthday

    with open("birthdays.json", "w") as file:
        json.dump(names_dictionary, file)

months_dictionary = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
                    }
months = []
with open("birthdays.json", "r") as file:
    names_dictionary = json.load(file)
    for birthday_string in names_dictionary.values():
        month = int(birthday_string.split("/")[1])
        months.append(months_dictionary[month])
print(Counter(months))

