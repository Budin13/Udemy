# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_list = []

my_pass = ""
for i in range(0, nr_letters):
    my_pass += random.choice(letters)
for i in range(0, nr_symbols):
    my_pass += random.choice(symbols)
for i in range(0, nr_numbers):
    my_pass += random.choice(numbers)

print("Your password could be " + my_pass)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_list = []
for i in range(0, nr_letters):
    pass_list.append(random.choice(letters))
for i in range(0, nr_symbols):
    pass_list.append(random.choice(symbols))
for i in range(0, nr_numbers):
    pass_list.append(random.choice(numbers))

random.shuffle(pass_list)
my_pass = ""
for i in pass_list:
    my_pass += i

print("\nYour password could be " + my_pass)
