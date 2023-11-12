import time
import itertools
import logging
from multiprocessing import Pool
from tqdm import tqdm
import bcrypt

# Set the character sets to use for generating passwords
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;':,.<>?/`~"

# Set the password criteria
MIN_PASSWORD_LENGTH = 8
MIN_UPPERCASE_LETTERS = 1
MIN_LOWERCASE_LETTERS = 1
MIN_NUMBERS = 1
MIN_SPECIAL_CHARACTERS = 1

def check_password_strength(password):
    # Check if the password meets the criteria
    if (
        len(password) >= MIN_PASSWORD_LENGTH
        and sum(1 for c in password if c.isupper()) >= MIN_UPPERCASE_LETTERS
        and sum(1 for c in password if c.islower()) >= MIN_LOWERCASE_LETTERS
        and sum(1 for c in password if c.isdigit()) >= MIN_NUMBERS
        and sum(1 for c in password if c in special_characters) >= MIN_SPECIAL_CHARACTERS
    ):
        return True
    return False

def brute_force_telus_shaw_wifi():
    password = ""
    target_password = b"SuperSecretPassword"  # Hashed target password

    # Define the character sets to use for generating passwords
    character_sets = [uppercase_letters, lowercase_letters, numbers, special_characters]

    # Set up logging
    logging.basicConfig(filename='brute_force.log', level=logging.INFO)

    # Set the maximum number of processes to use in parallel processing
    num_processes = 4

    # Generate passwords of varying lengths
    with Pool(processes=num_processes) as pool:
        for password_length in range(MIN_PASSWORD_LENGTH, len(target_password) + 1):
            # Generate all possible combinations of characters
            combinations = itertools.product(*character_sets, repeat=password_length)
            pbar = tqdm(total=len(character_sets)**password_length, unit=' Combination(s)', desc=f"Length: {password_length}")

            # Use multiprocessing to speed up the brute force process
            results = pool.imap(try_password, combinations)

            for result in results:
                if result is not None:
                    password = "".join(result)
                    pbar.close()
                    logging.info(f"Success! Password found: {password}")
                    print(f"Success! Password found: {password}")
                    return

                pbar.update()

            pbar.close()

    logging.info("Password not found.")
    print("Password not found.")

def try_password(combination):
    password = "".join(combination)
    if check_password_strength(password):
        # Add delay between each attempted password
        time.sleep(0.1)
        # Hash the attempted password and compare with the target password hash
        if bcrypt.checkpw(password.encode(), target_password):
            return combination

if __name__ == "__main__":
    brute_force_telus_shaw_wifi()
