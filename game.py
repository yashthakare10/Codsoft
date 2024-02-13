import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print("\nYour choice: {}".format(user_choice))
    print("Computer's choice: {}".format(computer_choice))
    print(result)

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

        user_choice = input("Enter your choice (1-3) or 4 to quit: ")

        if user_choice == '4':
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice in ['1', '2', '3']:
            user_choice = choices[int(user_choice) - 1]
            result = determine_winner(user_choice, computer_choice)
            display_result(user_choice, computer_choice, result)

            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("\nGame Over")
    print("Your score: {}".format(user_score))
    print("Computer's score: {}".format(computer_score))

if __name__ == "__main__":
    rock_paper_scissors()
