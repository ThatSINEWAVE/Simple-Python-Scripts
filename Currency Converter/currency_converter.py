import requests


def convert_currency(amount, from_currency, to_currency):
    api_key = 'YOUR_API_KEY'
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount


def main():
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency: ").upper()
    to_currency = input("Enter the target currency: ").upper()
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")


if __name__ == "__main__":
    main()
