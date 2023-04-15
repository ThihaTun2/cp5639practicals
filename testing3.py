import random

MENU = "Paper\nScissors\nRock\nQuit\nEnter a choice: "

picks = ["paper", "scissors", "rock"]

user_pick = input(MENU).lower()
while user_pick != "quit":

    computer_pick = random.choice(picks)
    print(f"\nYou chose {user_pick}, computer chose {computer_pick}.")

    while user_pick != "paper" and user_pick != "scissors" and user_pick != "rock":
        print("Invalid Input\n")
        user_pick = input(MENU).lower()

    if user_pick == computer_pick:
        result = "It's a DRAW"
    elif user_pick == "paper":
        if computer_pick == "rock":
            result = "YOU"
        else:
            result = "COMPUTER"
    elif user_pick == "scissors":
        if computer_pick == "paper":
            result = "YOU"
        else:
            result = "COMPUTER"
    else:
        if computer_pick == "scissors":
            result = "YOU"
        else:
            result = "COMPUTER"

    print(f"{result} WINS\n")

    user_pick = input(MENU).lower()