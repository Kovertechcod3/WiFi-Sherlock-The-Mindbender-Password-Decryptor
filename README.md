This project demonstrates a brute force attack on a Telus/Shaw wireless network password. It generates all possible combinations of characters from different character sets and checks if each generated password meets the specified criteria.

## Requirements

- Python 3
- tqdm library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/brute-force-telus-shaw-wifi.git
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the terminal or command prompt.

2. Navigate to the project directory:

   ```bash
   cd brute-force-telus-shaw-wifi
   ```

3. Modify the `target_password` variable in the `brute_force_telus_shaw_wifi.py` file with the actual network password you want to crack. Make sure to set the password as a hashed value using a secure password hashing algorithm like bcrypt.

4. Run the script:

   ```bash
   python brute_force_telus_shaw_wifi.py
   ```

   The script will start generating passwords of varying lengths and check if they meet the specified criteria. If a password is found that matches the target password, the script will display a success message and exit. Otherwise, it will display a failure message.

   **Note:** The brute force attack can take a long time depending on the length and complexity of the target password.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
