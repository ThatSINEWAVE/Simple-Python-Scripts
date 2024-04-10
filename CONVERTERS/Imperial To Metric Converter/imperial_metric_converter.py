import sys


def mk(miles):
    return miles * 1.60934


def km(km):
    return km * 0.621371


def fm(feet):
    return feet * 0.3048


def mf(meters):
    return meters * 3.28084


def main():
    if len(sys.argv) < 3:
        print("Usage: python imperialmetricconverter.py <conversion> <value>")
        print("Conversions: miles_to_km(mk), km_to_miles(km), feet_to_meters(fm), meters_to_feet(mf)")
        sys.exit(1)

    conversion = sys.argv[1]
    value = float(sys.argv[2])

    if conversion == "mk":
        result = mk(value)
        print(f"{value} miles is equal to {result} kilometers")
    elif conversion == "km":
        result = km(value)
        print(f"{value} kilometers is equal to {result} miles")
    elif conversion == "fm":
        result = fm(value)
        print(f"{value} feet is equal to {result} meters")
    elif conversion == "mf":
        result = mf(value)
        print(f"{value} meters is equal to {result} feet")
    else:
        print("Invalid conversion specified")


if __name__ == "__main__":
    main()
