import random

def generate_password(letters_input, numbers_input, symbols_input):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    for letter in range(0, letters_input):
        password.append((random.choice(letters)))
    for number in range(0, numbers_input):
        password.append(random.choice(numbers))
    for symbol in range(0, symbols_input):
        password.append(random.choice(symbols))

    random.shuffle(password)
    final_password = ""
    for char in password:
        final_password = final_password + char

    return final_password
