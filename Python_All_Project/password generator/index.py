# password generator

import random

import string

def generator_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password =''.join(random.choice(characters) for _ in range(length))
    return password

    #user input for password length

length = int(input("Enter the length of the password: "))

password = generator_password(length)

print("Generated password:", password)

