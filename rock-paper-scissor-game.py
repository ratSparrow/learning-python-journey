import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(computer, player):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return  "Tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "scissors":
      return "Scissors cuts paper! You lose."
    else:
      return "Paper covers rock! You win!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["computer"], choices["player"])
print (result)
    