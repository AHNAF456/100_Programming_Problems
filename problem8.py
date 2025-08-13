import random
while True:
    player=input("Choose an option(rock,paper,scissor):").lower()
    options=["rock","paper","scissor"]
    computer=random.choice(options)
    if player not in options:
        print("You choosed an wrong option")
        continue
    elif player in options:
        if computer == player:
            print("Draw")
        elif computer =="rock" and player == "paper":
            print("You win")
        elif computer == "paper" and player == "scissor":
            print("You win")
        elif computer == "scissor" and player == "rock":
            print("You win")
        else:
            print("You lose")
    print(f"Computer:{computer} player:{player}")
    number=input("Do you want to play again?:").lower()
    if number == "yes":
        continue
    else:
        break


