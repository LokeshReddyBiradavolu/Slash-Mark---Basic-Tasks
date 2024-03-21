import string
import random

def generate_password(characters_number):
    # store all characters in strings
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # calculate the number of characters for each category
    num_letters = round(characters_number * 0.6)
    num_digits_punctuations = characters_number - num_letters

    # generate password
    password = ''.join(random.choices(lowercase_letters, k=num_letters))
    password += ''.join(random.choices(uppercase_letters, k=num_letters))
    password += ''.join(random.choices(digits + punctuation, k=num_digits_punctuations))

    # shuffle password
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

while True:
    user_input = input("Enter the number of characters for your password (type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your number should be at least 8.")
        else:
            password = generate_password(characters_number)
            print("Strong Password:", password)
    except ValueError:
        print("Please enter a valid number or type 'quit' to exit.")
