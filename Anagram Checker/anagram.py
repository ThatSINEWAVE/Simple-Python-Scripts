def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    if is_anagram(word1, word2):
        print("Yes, the words are anagrams of each other!")
    else:
        print("No, the words are not anagrams.")


if __name__ == "__main__":
    main()
