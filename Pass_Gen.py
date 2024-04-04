#import random and string 
import random
import string

def generate_password(length):
    """
    generate random password
    
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+=-[]{}|;:,.<>?~"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    
def get_password_length():
    """
    get password length from the user
    
    """
    

def generate_password_with_options(length, include_symbols=False, include_numbers=False, include_uppercase=False, include_lowercase=False):
    """
    Include options for password
    
    """
    characters = ''
    if include_symbols:
        characters += "!@#$%^&*()_+=-[]{}|;:,.<>?~"
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        print("Please include at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password(password):
    """
    Display the password
    
    """
    print("Generated Password:", password)

# Main program
if __name__ == "__main__":
    """
    Main part
    
    """
    length = get_password_length()
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    password = generate_password_with_options(length, include_symbols, include_numbers, include_uppercase, include_lowercase)
    display_password(password)
