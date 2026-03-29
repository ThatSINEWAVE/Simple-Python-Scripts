import math

plus_minus = "\u00B1"

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if a == 0 and b != 0:
        x = -c/b
        return x
    elif a == 0 and b == 0 and c == 0:
        return "infinite solutions"
    elif a == 0 and b == 0 and c != 0:
        return "no solutions"
    else:
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Roots: {root1, root2}"
        elif discriminant == 0:
            root = -b / (2*a)
            return f"Roots: {root}"
        else:
            positive_number = abs(discriminant)
            complex_form = f"({-b}{plus_minus}{math.sqrt(positive_number)}i)/{2*a}"
            return f"No real roots\n{complex_form}"

def main():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    roots = solve_quadratic(a, b, c)
    print(f"{roots}")  #Output


if __name__ == "__main__":
    main()
