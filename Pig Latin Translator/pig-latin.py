def translate_to_pig_latin(word):
    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"


def main():
    word = input("Enter a word or phrase to translate to Pig Latin: ")
    translated_word = " ".join(translate_to_pig_latin(w) for w in word.split())
    print("Translated:", translated_word)


if __name__ == "__main__":
    main()
