def generate_fibonacci_sequence(terms):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < terms:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence


def main():
    terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci_sequence(terms)
    print("Fibonacci sequence:", fibonacci_sequence)


if __name__ == "__main__":
    main()
