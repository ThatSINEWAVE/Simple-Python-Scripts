import random


def play_game(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print(f"Computer chooses: {computer_choice}")
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice!")
    else:
        print(play_game(user_choice))


if __name__ == "__main__":
    main()
