import random 

def get_choices():
    player_choice = input("Enter your choice(rock, paper, scissors): ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices 

def checkwin(player, computer):
    print(f"you choose {player} computer choose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes scissors, you win!"    
    else: 
        return "Paper covers Rock, you lose!"  
    if computer == "Paper" and player == "Rock": 
        return "Paper covers Rock, you lose!"
    else:
        return "Scissors cuts paper, you win!"
    

choices = get_choices()

results = checkwin(choices["player"], choices["computer"])

print(results)

        

