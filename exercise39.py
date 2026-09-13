import datetime
name = input("Enter your name ")
age = int(input("Enter your age "))
year_when_100 = (datetime.datetime.now()).year + 100 - age
print(f"{name}, your age will hit 100 in {year_when_100}")