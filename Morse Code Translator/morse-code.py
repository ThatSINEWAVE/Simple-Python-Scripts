MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        else:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code


def morse_to_text(morse_code):
    text = ''
    morse_code += ' '
    char = ''
    for symbol in morse_code:
        if symbol != ' ':
            i = 0
            char += symbol
        else:
            i += 1
            if i == 2:
                text += ' '
            else:
                text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(char)]
                char = ''
    return text


def main():
    choice = input("Enter '1' to convert text to Morse code or '2' to convert Morse code to text: ")
    if choice == '1':
        text = input("Enter the text to convert to Morse code: ")
        morse_code = text_to_morse(text)
        print("Morse code:", morse_code)
    elif choice == '2':
        morse_code = input("Enter the Morse code to convert to text (use '.' for dot and '-' for dash): ")
        text = morse_to_text(morse_code)
        print("Text:", text)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
