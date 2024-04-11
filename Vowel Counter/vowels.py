def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def main():
    text = input("Enter a text: ")
    vowel_count = count_vowels(text)
    print(f"The number of vowels in the text is: {vowel_count}")


if __name__ == "__main__":
    main()
