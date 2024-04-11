def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


def main():
    binary = input("Enter a binary number: ")
    decimal = binary_to_decimal(binary)
    print(f"The decimal equivalent of {binary} is {decimal}.")


if __name__ == "__main__":
    main()
