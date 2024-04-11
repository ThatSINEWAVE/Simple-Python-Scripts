def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as f:
        plaintext = f.read()
    encrypted_text = caesar_cipher(plaintext, key)
    with open(output_file, 'w') as f:
        f.write(encrypted_text)


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r') as f:
        ciphertext = f.read()
    decrypted_text = caesar_cipher(ciphertext, key, decrypt=True)
    with open(output_file, 'w') as f:
        f.write(decrypted_text)


def main():
    choice = input("Enter '1' to encrypt a file or '2' to decrypt a file: ")
    if choice == '1':
        input_file = input("Enter the path to the file to encrypt: ")
        output_file = input("Enter the path to save the encrypted file: ")
        key = int(input("Enter the encryption key (shift value): "))
        encrypt_file(input_file, output_file, key)
        print("File encrypted successfully.")
    elif choice == '2':
        input_file = input("Enter the path to the file to decrypt: ")
        output_file = input("Enter the path to save the decrypted file: ")
        key = int(input("Enter the decryption key (shift value): "))
        decrypt_file(input_file, output_file, key)
        print("File decrypted successfully.")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
