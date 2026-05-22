def is_palindrome_number(number):
    return str(number) == str(number)[::-1]


def main():
    number = int(input("Enter a number to check for palindrome: "))
    try:
        if is_palindrome_number(number):
            print("Yes, it's a palindrome!")
        else:
            print("No, it's not a palindrome.")

    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()
