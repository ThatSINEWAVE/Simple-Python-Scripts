import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Yes, it's a valid email address!")
    else:
        print("No, it's not a valid email address.")


if __name__ == "__main__":
    main()
