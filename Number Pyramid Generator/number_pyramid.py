def generate_number_pyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i), end="")
        for j in range(1, i * 2):
            print(j, end="")
        print()


def main():
    height = int(input("Enter the height of the number pyramid: "))
    generate_number_pyramid(height)


if __name__ == "__main__":
    main()
