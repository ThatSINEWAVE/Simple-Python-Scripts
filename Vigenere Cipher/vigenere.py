import re

def main():
    alpha_choice = "abc"
    while not alpha_choice in ["", "ascii", "standard"]:
        alpha_choice = input("pick an alphabet: ascii (default)/ standard (26 letter)> ")
    if alpha_choice in ["", "ascii"]:
        alphabet = [chr(i) for i in range(0x20,0x7f)]
    else:
        alphabet = [chr(i) for i in range(0x61, 0x7b)]

    mode = ""
    while not mode in ["e","d", "q"]:
        mode = input("encode (e)/decode (d)/quit (q) > ")

    if mode == "q":
        return

    elif mode == "e" and alpha_choice in ["", "ascii"]:
        user_input = input("string to encode > ")
        key = input("enter key > ")
        key_padded = [key[i % len(key)] for i in range(len(user_input))]
        decrypted = ''.join([alphabet[((ord(user_input[i]) - 0x20) + (ord(key_padded[i]) - 0x20)) % len(alphabet)] for i in range(len(user_input))])
        print(f"output: {decrypted}")
    elif mode == "d" and alpha_choice in ["", "ascii"]:
        user_input = input("string to decode > ")
        key = input("enter key > ")
        key_padded = [key[i % len(key)] for i in range(len(user_input))]
        decrypted = ''.join([alphabet[((ord(user_input[i]) - 0x20) - (ord(key_padded[i]) - 0x20)) % len(alphabet)] for i in range(len(user_input))])
        print(f"output: {decrypted}")
    elif mode == "e":
        user_input = input("string to encode > ").lower()
        key = input("enter key > ")
        key_cleaned = re.sub('[^A-Za-z]', '', key)
        key_cleaned = key_cleaned.lower()
        key_padded = ""
        k = 0
        for c in user_input:
            if c.isalpha():
                key_padded += key_cleaned[k]
                k += 1
                if k >= len(key_cleaned):
                    k = 0
            else:
                key_padded += ' '
        result = []
        for i in range(len(user_input)):
            if user_input[i].isalpha():
                result.append(alphabet[((ord(user_input[i]) - 0x61) + (ord(key_padded[i]) - 0x61)) % len(alphabet)])
            else:
                result.append(user_input[i])
        decrypted = ''.join(result)
        print(f"output: {decrypted}")

        
    elif mode == "d":
        user_input = input("string to decode > ").lower()
        key = input("enter key > ")
        key_cleaned = re.sub('[^A-Za-z]', '', key)
        key_cleaned = key_cleaned.lower()
        key_padded = ""
        k = 0
        for c in user_input:
            if c.isalpha():
                key_padded += key_cleaned[k]
                k += 1
                if k >= len(key_cleaned):
                    k = 0
            else:
                key_padded += ' '
        result = []
        for i in range(len(user_input)):
            if user_input[i].isalpha():
                result.append(alphabet[((ord(user_input[i]) - 0x61) - (ord(key_padded[i]) - 0x61)) % len(alphabet)])
            else:
                result.append(user_input[i])
        decrypted = ''.join(result)
        print(f"output: {decrypted}")

if __name__ == "__main__":
    main()
