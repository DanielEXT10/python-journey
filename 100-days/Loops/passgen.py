
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


    nr_letters = int(input("How many letters would you like in your password?\n"))

    nr_numbers = int(input("How many numbers would you like on your password\n"))
    nr_symbols = int(input("How many symbols would you like on your password\n"))

    letters_list = []
    for i in range(nr_letters):
        element = random.choice(letters)
        letters_list.append(element)

    numbers_list = []
    for i in range(nr_numbers):
        element = random.choice(numbers)
        numbers_list.append(element)

    symbols_list = []
    for i in range(nr_symbols):
        element = random.choice(symbols)
        symbols_list.append(element)

    password = letters_list + numbers_list + symbols_list
    random.shuffle(password)

    password = "".join(password)
    print(f"Your generated password is: {password}")


generate_password()