import random
import argparse

def generate_password(ssid):
    if ssid == "2WIREXXX":
        return str(random.randint(0, 9999999999)).zfill(10)
    elif ssid == "3MobileWiFi":
        characters = "0123456789abcdefghijklmnopqrstuvwxyz"
        return ''.join(random.choice(characters) for _ in range(8))
    elif ssid == "3Wireless-Modem-XXXX":
        return '{:04x}'.format(random.randint(0, 65535))
    elif ssid == "Alice_XXXXXXXX":
        characters = "0123456789abcdefghijklmnopqrstuvwxyz"
        return ''.join(random.choice(characters) for _ in range(24))
    elif ssid == "AOLBB-XXXXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(8))
    elif ssid == "ATT###":
        return str(random.randint(0, 9999999999)).zfill(10)
    elif ssid == "ATTxxxx 0000":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(10))
    elif ssid == "ATTxxxxxxx":
        characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+"
        return ''.join(random.choice(characters) for _ in range(12))
    elif ssid == "belkin.xxx":
        characters = "23456789abcdef"
        return ''.join(random.choice(characters) for _ in range(8))
    elif ssid == "belkin.xxxx":
        return '{:04x}'.format(random.randint(0, 65535))
    elif ssid == "Belkin.XXXX":
        return '{:04X}'.format(random.randint(0, 65535))
    elif ssid == "Belkin_XXXXXX":
        return '{:06X}'.format(random.randint(0, 16777215))
    elif ssid == "BTHub3-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(10))
    elif ssid == "BTHub4-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(10))
    elif ssid == "BTHub5-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(10))
    elif ssid == "BTHub6-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(10))
    elif ssid == "D-Link-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(8))
    elif ssid == "DLink-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(8))
    elif ssid == "EircomXXXXXXX":
        characters = "0123456789abcdefghijklmnopqrstuvwxyz"
        return ''.join(random.choice(characters) for _ in range(10))
    elif ssid == "HH3A-XXXX":
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(characters) for _ in range(8))
    else:
        return "No password format found for the given SSID."

def main():
    parser = argparse.ArgumentParser(description='Password Generator for different SSID formats')
    parser.add_argument('ssid', type=str, help='SSID name')
    args = parser.parse_args()

    password = generate_password(args.ssid)
    if password.startswith("No password format"):
        print(password)
    else:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
