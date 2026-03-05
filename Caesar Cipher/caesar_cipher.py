"""
A Caesar cipher encrypter/decrypter.

"The Caesar cipher is one of the simplest and most widely known
encryption techniques used in cryptography. It is a type of
substitution cipher in which each letter in the plaintext is replaced by
a letter some fixed number of positions along the alphabet. For example,
with a left shift of 3, D would be replaced by A, E would become B, and
so on. The method is named after Julius Caesar, who used it in his
private correspondence."

(Extracted from Wikipedia: https://en.wikipedia.org/wiki/Caesar_cipher)
        
Example with a left shift of 3 (key=-3):
    'Hello, world!' → 'Ebiil, tloia!'
    'This is an English sentence.' → 'Qefp fp xk Bkdifpe pbkqbkzb.'
"""

import string


def cipher(text: str, key: int) -> str:
    """Cipher a given alphabetical plaintext using a Caesar cipher.

    Non-english letters are ignored.

    Args:
        text (str): the plaintext to be ciphered
        key (int): The number of positions by which each alphabetical character
            in `text` is shifted along the English alphabet. Positive values
            shift to the right; negative values shift to the left.

    Returns:
        str: the encrypted ciphertext
    """
    if not isinstance(key, int):
        raise TypeError("Parameter 'key' must be an integer.")

    output = ""
    table = cipher_table(key)
    for char in text:
        if char not in string.ascii_letters:
            output += char
        else:
            new = table[char.lower()]
            output += new.lower() if char.islower() else new.upper()
    return output


def decipher(text: str, key: int) -> str:
    """Decipher ciphertext encrypted using a Caesar cipher.

    Args:
        text (str): The ciphertext to be deciphered.
        key (int): The number of positions by which each alphabetical character
            in `text` was shifted along the English alphabet during encryption.
            Positive values indicate a rightward shift; negative values indicate
            a leftward shift.

    Returns:
        str: the decrypted plaintext
    """
    if not isinstance(key, int):
        raise TypeError("Parameter 'key' must be an integer.")
    return cipher(text, -key)


def cipher_table(steps: int) -> dict[str, str]:
    """Generate a Caesar cipher substitution table.

    Creates a mapping from each lowercase English letter to the letter
    obtained by shifting it `steps` positions along the alphabet.
    Positive values shift letters to the right; negative values shift
    letters to the left. Shift values larger than the alphabet length
    are normalized automatically.

    Args:
        steps (int): The number of positions to shift each letter in the
            alphabet. Positive values indicate a rightward shift, while
            negative values indicate a leftward shift.

    Returns:
        dict[str, str]: A dictionary mapping each lowercase English letter
        to its corresponding shifted letter.
    """
    if not isinstance(steps, int):
        raise TypeError("Parameter 'key' must be an integer.")

    alphabet = string.ascii_lowercase

    # Calculate the effective shift amount relative to the list length.
    # This handles large steps (e.g., n=10 steps for a list of 3 items)
    # and standardizes the index to the range 0 to len(data_list).
    effective_steps = steps % len(alphabet)

    try:
        rotated_alphabet = (alphabet[effective_steps:]
                            + alphabet[:effective_steps])
    except TypeError:
        raise TypeError("Parameter 'steps' must be an integer.")

    output = dict(zip(alphabet, rotated_alphabet))
    return output


if __name__ == "__main__":
    from time import sleep

    print("\nWelcome to the Caesar cipher encrypter/decrypter!\n")
    sleep(0.5)
    print(
        "* --------------------------------------- *\n"
        "The Caesar cipher is one of the simplest and most widely\n"
        "known encryption techniques used in cryptography. It is\n"
        "a type of substitution cipher in which each letter in the\n"
        "plaintext is replaced by a letter some fixed number (key)\n"
        "of positions along the alphabet.\n"
        
        "\nFor example, with a left shift of 3, D would be replaced\n"
        "by A, E would become B, and so on. The method is named after\n"
        "Julius Caesar, who used it in his private correspondence.\n"
        
        "\n(Extracted from Wikipedia: https://en.wikipedia.org/wiki/Caesar_cipher)\n"
        
        "\nExample with a left shift of 3 (key=-3):\n"
        "\t'Hello, world!' → 'Ebiil, tloia!'\n"
        "\t'This is an English sentence.' → 'Qefp fp xk Bkdifpe pbkqbkzb.'"
        "\n* --------------------------------------- *"
    )

    while True:
        print("\nChoose an option:")
        print("1) Encrypt text with Caesar cipher")
        print("2) Decrypt ciphered text")
        print("3) Quit")

        match input("> ").strip():

            case '1':
                while True:
                    switching = False
                    
                    txt = input(
                        "\nEnter text to encrypt ('/' to return to menu): "
                    )
                    if txt.strip() == '/':
                        break
                        
                    while True:
                        ky = input("Enter key ('/' to return to menu): ")
                        
                        if ky.strip() == '/':
                            switching = True
                            break
                            
                        try:
                            ky = int(ky)
                        except ValueError:
                            print(
                                "\nInvalid choice. Please enter an integer.\n"
                            )
                            sleep(0.5)
                        else:
                            break
                            
                    if switching:
                        break
                        
                    print(f"\nEncrypted text:")
                    print(cipher(txt, ky))

            case '2':
                while True:
                    switching = False
                    
                    txt = input(
                        "\nEnter text to decrypt ('/' to return to menu): "
                    )
                    if txt.strip() == '/':
                        break
                    
                    while True:
                        ky = input("Enter key ('/' to return to menu): ")
                        
                        if ky.strip() == '/':
                            switching = True
                            break
                        
                        try:
                            ky = int(ky)
                        except ValueError:
                            print(
                                "\nInvalid choice. Please enter an integer.\n"
                            )
                            sleep(0.5)
                        else:
                            break
                    
                    if switching:
                        break
                    
                    print(f"\nDecrypted text:")
                    print(decipher(txt, ky))

            case '3':
                print("\nBye!")
                break

            case _:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
                sleep(0.5)
