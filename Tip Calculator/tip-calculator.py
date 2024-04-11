def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return total_amount


def main():
    bill_amount = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage: "))
    total_amount = calculate_tip(bill_amount, tip_percentage)
    print(f"Total amount including tip: ${total_amount:.2f}")


if __name__ == "__main__":
    main()
