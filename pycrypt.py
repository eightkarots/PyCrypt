import os
import base64
from cryptography.fernet import Fernet

def app_title():
    print("\n\033[95mPyCrypt\033[0m")

def main():
    while True:
        print("\033[H\033[J") #clears screen
        app_title()
        print("\n1. Encrypt File (No Key)")
        print("2. Encrypt File (Key)")
        print("3. Decrypt File (Display)")
        print("4. Decrypt File (Store)")
        print("5. About PyCrypt")
        print("6. Exit\n")
        choice = input("Choose an option: ").strip()
        print("\033[H\033[J") # clears screen
        if choice not in ['1','2','3','4','5','6']:
            continue
        #choice 1
        if choice == '1':
            app_title()
            file_path = input("\nEnter file path: ").strip()
            if not os.path.isfile(file_path):
                print("\033[H\033[J") #clears screen
                app_title()
                print("\nFile does not exist. Please try again.")
                input("\nPress Enter to continue back to menu...")
                if input:
                    continue
            if input:
                print("\033[H\033[J") #clears screen
                app_title()
            password = input("\nEnter the key for encryption/decryption: ")
            key = generate_key(password)
            encrypt_file(file_path, key)
            continue
        #choice 2
        if choice == '2':
            app_title()
            file_path = input("\nEnter file path: ").strip()
            if not os.path.isfile(file_path):
                print("\033[H\033[J") #clears screen
                app_title()
                print("\nFile does not exist. Please try again.")
                input("\nPress Enter to continue back to menu...")
                if input:
                    continue
            if input:
                print("\033[H\033[J") #clears screen
                app_title()
            password = input("\nEnter the key for encryption/decryption: ")
            key = generate_key(password)
            save_key(file_path, password)
            encrypt_file(file_path, key)
            continue
        #choice 3
        if choice == '3':
            app_title()
            file_path = input("\nEnter file path: ").strip()
            if not os.path.isfile(file_path):
                print("\033[H\033[J") #clears screen
                app_title()
                print("\nFile does not exist. Please try again.")
                input("\nPress Enter to continue back to menu...")
                if input:
                    continue
            if input:
                print("\033[H\033[J") #clears screen
                app_title()
            password = input("\nEnter the key for encryption/decryption: ")
            key = generate_key(password)
            decrypt_file_ram(file_path, key)
            continue
        #choice 4
        if choice == '4':
            app_title()
            file_path = input("\nEnter file path: ").strip()
            if not os.path.isfile(file_path):
                print("\033[H\033[J") #clears screen
                app_title()
                print("\nFile does not exist. Please try again.")
                input("\nPress Enter to continue back to menu...")
                if input:
                    continue
            if input:
                print("\033[H\033[J") #clears screen
                app_title()
            password = input("\nEnter the key for encryption/decryption: ")
            key = generate_key(password)
            decrypt_file_export(file_path, key)
            continue
        #choice 5
        if choice == '5':
            app_title()
            print("")
            about()
            print("")
            input("Press Enter to continue back to menu...")
            if input:
                print("\033[H\033[J") #clears screen
                continue
        if choice == '6':
            os._exit(0)
        else:
            try:
                main()
            except Exception as e:
                print("\033[H\033[J") #clears screen
                app_title()
                print("\nDecryption failed. Ensure the correct key is used.")
                print(f"\nError: {e}")
                input("\nPress Enter to continue back to menu...")
                if input:
                    print("\033[H\033[J") #clears screen
                    continue
        break

#Generates a key from a password
def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(password.encode('utf-8').ljust(32)[:32])

#Saves the key to a separate .txt file
def save_key(file_path: str, key_text: str):
    key_file_path = f"{file_path}-key.txt"
    with open(key_file_path, 'w') as key_file:
        key_file.write(key_text)
    print("\033[H\033[J") #clears screen
    app_title()
    print(f"\nKey saved to {key_file_path}")
    input("\nPress Enter to encrypt file...")

#Encrypts the contents of the given file using the provided key
def encrypt_file(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    print("\033[H\033[J") #clears screen
    app_title()
    print("\nFile encrypted successfully.")
    input("\nPress Enter to continue back to menu...")

#Displays the decrypted contents of the given file using the provided key
def decrypt_file_ram(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    print("\033[H\033[J") #clears screen
    app_title()
    print("\nDecrypted Content:\n")
    print("\033[92m" + decrypted_data.decode('utf-8') + "\033[0m")
    input("\nPress Enter to continue back to menu...")

#Decrypts the contents of the given file using the provided key
def decrypt_file_export(file_path: str, key: bytes):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
    print("\033[H\033[J") #clears screen
    app_title()
    print("\nFile decrypted successfully.")
    input("\nPress Enter to continue back to menu...")
    if input:
        main()

#About info page
def about():
    print("Hi! This program was coded by eightkarots.")
    print("\nPyCrypt allows you to both encrypt and decrypt any file type of your choosing (Anything other than text files will not work with the display mode to decrypt).")
    print("\nWhen encrypting a file, you will be prompted to set a key which will be used later for decryption.")
    print("There are two modes for encryption, the no key mode (recommended) will not include a text file containing the key. The key mode (not recommended) will include one.")
    print("\nThe display mode for decryption will display the decrypted contents of text files only.")
    print("The store mode for decryption will alter the contents of the original file back to its original unencrypted state.")
    print("\nCompliments (or complaints) to the chef can be sent down to \033]8;;https://github.com/eightkarots\033\\Github\033]8;;\033\\")

main()
