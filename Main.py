import itertools
import subprocess

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

def get_wifi_networks():
    command = ["nmcli", "-f", "SSID", "device", "wifi", "list"]
    output = subprocess.run(command, capture_output=True, text=True)
    output_lines = output.stdout.splitlines()
    wifi_networks = [line.split()[-1] for line in output_lines[1:]]
    return wifi_networks

def select_wifi_network(wifi_networks):
    print("Available WiFi Networks:")
    for i, network in enumerate(wifi_networks, start=1):
        print(f"{i}. {network}")

    while True:
        selection = input("Enter the number of the WiFi network you want to crack: ")
        try:
            selection_index = int(selection) - 1
            if selection_index >= 0 and selection_index < len(wifi_networks):
                return wifi_networks[selection_index]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    wifi_networks = get_wifi_networks()
    if len(wifi_networks) == 0:
        print("No WiFi networks found. Please make sure your WiFi adapter is enabled.")
        return

    selected_network = select_wifi_network(wifi_networks)
    target_password = selected_network.encode()

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

    print("Password not found. Keep trying!")

if __name__ == "__main__":
    main()
