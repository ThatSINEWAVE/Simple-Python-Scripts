import random


def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        result = random.randint(1, sides)
        results.append(result)
    return results


def main():
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))
    print("Rolling the dice...")
    results = roll_dice(sides, rolls)
    print("Results:", results)


if __name__ == "__main__":
    main()
