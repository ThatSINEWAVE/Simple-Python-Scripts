def word_count(text):
    word_count = len(text.split())
    char_count = len(text)
    line_count = text.count('\n') + 1
    return word_count, char_count, line_count


def main():
    text = input("Enter your text:\n")
    words, chars, lines = word_count(text)
    print(f"Word count: {words}")
    print(f"Character count: {chars}")
    print(f"Line count: {lines}")


if __name__ == "__main__":
    main()
