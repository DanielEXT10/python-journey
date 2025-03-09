import random
import string

def generate_password():
    secure_random = random.SystemRandom()

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list('!@#$%&*()')

    # Function to safely get user input
    def get_positive_integer(prompt):
        while True:
            try:
                value =int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Please enter a non-negative number")
            except ValueError:
                print("Invalid input please insert a valid one")
    
    # Get user input with validation
    nr_letters = get_positive_integer("How many letters would you like in your password?\n")
    nr_numbers = get_positive_integer("How many numbers would you like in your password?\n")
    nr_symbols = get_positive_integer("How many symbols would you like in your password?\n")

    if nr_letters + nr_numbers + nr_symbols == 0:
        print("You must need to include at least one character on your password")
        return
    
    #Get password elements
    password_list = (
        [secure_random.choice(letters) for i in range(nr_letters)] +
        [secure_random.choice(numbers) for i in range(nr_numbers)] + 
        [secure_random.choice(symbols) for i in range(nr_symbols)]
    )

    #shuffle password
    secure_random.shuffle(password_list)

    #convert to string
    password = "".join(password_list)
    print(f"\n🔒 Your generated password: {password}\n")

generate_password()