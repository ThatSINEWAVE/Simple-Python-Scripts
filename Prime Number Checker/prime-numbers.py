def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("Yes, it's a prime number!")
    else:
        print("No, it's not a prime number.")


if __name__ == "__main__":
    main()
