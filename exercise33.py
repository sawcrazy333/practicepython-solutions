names_dictionary = {
                    "Wiktor": "05.04.2007",
                    "Nadia": "11.07.2007",
                    "Bruno": "04.09.2007"
                    }
print(f"Welcome to the birthday dictionary. We know the birthdays of: ")
for _ in names_dictionary:
    print(_)
name = input("Who's birthday do you want to look up? ")
if name in names_dictionary:
    print(f"The birthday of {name} is {names_dictionary[name]}")
else:
    print(f"{name} is not in the dictionary.")