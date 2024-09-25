import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+"

all_characters = characters + numbers + special_characters
password = ""

password += random.choice(characters.upper())
password += random.choice(numbers) # Ensure at least one special character
password += random.choice(special_characters)
    
while len(password) < 12:
    password += random.choice(all_characters)
    
    # Shuffle the password to ensure randomness
    password = list(password)
    random.shuffle(password)
    print("".join(password))
