def main():
    alphabet = [chr(i) for i in range(0x20,0x7f)]
    mode = ""
    while not mode in ["e","d", "q"]:
        mode = input("encode (e)/decode (d)/quit (q) > ")

    if mode == "q":
        return

    elif mode == "e":
        user_input = input("string to encode > ")
        key = input("enter key > ")
        key_padded = [key[i % len(key)] for i in range(len(user_input))]
        decrypted = ''.join([alphabet[((ord(user_input[i]) - 0x20) + (ord(key_padded[i]) - 0x20)) % len(alphabet)] for i in range(len(user_input))])
        print(f"output: {decrypted}")
    elif mode == "d":
        user_input = input("string to decode > ")
        key = input("enter key > ")
        key_padded = [key[i % len(key)] for i in range(len(user_input))]
        decrypted = ''.join([alphabet[((ord(user_input[i]) - 0x20) - (ord(key_padded[i]) - 0x20)) % len(alphabet)] for i in range(len(user_input))])
        print(f"output: {decrypted}")

if __name__ == "__main__":
    main()
