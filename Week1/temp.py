import random
import string
import argparse

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    char_pool = ''
    if use_uppercase:
        char_pool += upper
    if use_lowercase:
        char_pool += lower
    if use_digits:
        char_pool += digits
    if use_special:
        char_pool += special

    if not char_pool:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random Password Generator")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")

    args = parser.parse_args()

    password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
    print(f"Generated Password: {password}")



