# Pwned Password Checker
A program that uses the [Pwned Passwords API](https://haveibeenpwned.com/API/v3) to check if a password has previously been exposed in data breaches.

# Usage
Run the script by providing the path to a text file containing the passwords you want to check. The program will only send the first 5 characters of the passwords SHA-1 hash to the API, so looking up your passwords this way will be especially safe! :)
```bash
$ python3 passwordchecker.py passwords.txt
```