import random

def get_choices():
    player_choice = input("Enter a choice: rock, paper, scissors: ")
    choice = ["paper", "rock", "scissors"]
    computer_choice = random.choice(choice)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if (player == computer):
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper takes rock, you loose!"
        else:
            return "Rock takes scissors, you win!"
    elif player == "paper":
        if computer == "rock":
            return "Paper takes rock, you win!"
        else:
            return "Scissors takes paper, you loose!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock takes scissors, you loose!"
        else:
            return "Scissors takes paper, you win!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print (result)