def is_palindrome_number(number):
    return str(number) == str(number)[::-1]


def main():
    number = input("Enter a number to check for palindrome: ")
    if is_palindrome_number(number):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")


if __name__ == "__main__":
    main()
