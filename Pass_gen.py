import random

class InvalidSSIDError(Exception):
    def __init__(self, message="Invalid SSID."):
        self.message = message
        super().__init__(self.message)

class PasswordFormatNotFoundError(Exception):
    def __init__(self, message="No password format found for the given SSID."):
        self.message = message
        super().__init__(self.message)

# Dictionary mapping SSID formats to their corresponding password generation logic
password_formats = {
    "TELUSXXXX": lambda: ''.join(random.choice("0123456789") for _ in range(4)),
    # Add more Telus router SSID formats and their corresponding password generation logic here
}

def generate_password(ssid):
    if isinstance(ssid, str) and ssid.strip():
        if ssid in password_formats:
            return password_formats[ssid]()
        else:
            raise PasswordFormatNotFoundError
    else:
        raise InvalidSSIDError

def add_password_format(ssid, password_generator):
    if isinstance(ssid, str) and ssid.strip() and callable(password_generator):
        # Enforce password constraints
        def password_wrapper():
            password = password_generator()
            # Add any additional password constraints here
            return password

        password_formats[ssid] = password_wrapper
        return True
    else:
        return False

# Testing the code
ssid = input("Enter the Telus router SSID: ")
try:
    password = generate_password(ssid)
    print("Generated password:", password)
except InvalidSSIDError:
    print("Invalid SSID.")
except PasswordFormatNotFoundError:
    print("No password format found for the given SSID.")
