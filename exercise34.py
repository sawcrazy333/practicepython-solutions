import json

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
