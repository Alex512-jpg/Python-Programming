import json
import os

# XOR cipher key
KEY = 'mysecretkey'

def xor_cipher(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def save_credentials(resource, username, password):
    credentials = {}
    if os.path.exists("credentials.json"):
        with open("credentials.json", "r") as file:
            credentials = json.load(file)
    
    credentials[username] = xor_cipher(password, KEY)
    
    with open("credentials.json", "w") as file:
        json.dump(credentials, file, indent=4)

def retrieve_credentials(username):
    if not os.path.exists("credentials.json"):
        return None
    
    with open("credentials.json", "r") as file:
        credentials = json.load(file)
    encrypted_password = credentials.get(username)
    return xor_cipher(encrypted_password, KEY) if encrypted_password else None

def main():
    while True:
        action = input("Would you like to (save/retrieve/exit)? ").lower().strip()
        
        if action == "save":
            resource = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_credentials(resource, username, password)
            print("Credentials saved.")
        
        elif action == "retrieve":
            resource = input("Enter website:\n")
            username = input("Enter username:\n")
            retrieve_credentials(password)
            print(f"username and password for {resource}: {username if username else 'Not found.'} {password if password else 'Not found'}")
        
        elif action == "exit":
            break
        
        else:
            print("Invalid action. Please choose 'save', 'retrieve', or 'exit'.")

if __name__ == "__main__":
    main()
