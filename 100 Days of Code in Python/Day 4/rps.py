import random
#getting user choice
player_choice = input("Rock... Paper... Scissors... GO!\n")
player_choice = player_choice.lower()
options = ["rock","paper","scissors"]
bot_choice = random.choice(options)
#evaluating result based on player choice
if player_choice==bot_choice: #Draw Condition
    print("It's a Draw")
else:
    if player_choice=="scissors": # player chose scissors
        if bot_choice == "paper":
            print("You Won!")
        else:
            print("Bot Won :)")
    elif player_choice=="paper": # player chose paper
        if bot_choice == "rock":
            print("You Won!")
        else:
            print("Bot Won :)")
    elif  player_choice == "rock": # player chose rock
        if bot_choice=="scissors":
            print("You Won!")
        else:
            print("Bot Won :)")
    else:
        print("Please enter either rock, paper or scissors")