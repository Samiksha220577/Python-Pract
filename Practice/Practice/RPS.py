import random

def play_game():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

    while user_choice not in choices:
        user_choice = input("Invalid choice. Enter your choice (Rock, Paper, Scissors): ").capitalize()

    print(f"\nComputer chose: {computer_choice}")
    print(f"You chose: {user_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        print("You win!")
    else:
        print("Computer wins!")

play_game()