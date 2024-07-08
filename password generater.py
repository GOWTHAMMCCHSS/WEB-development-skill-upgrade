print("\t\tPASSWORD GENERATOR")
print("\t\t******************")

import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for the password length
password_length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(password_length)
print(f"Generated password: {password}")
