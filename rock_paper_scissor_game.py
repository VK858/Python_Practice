import random

user_wins = 0
computer_wins = 0
draw = 0
options = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Type rock/paper/scissors or Q to quit: ")
    if user_input.lower() == "q":
        break
    
    if user_input.lower() not in options:
        continue
    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input.lower() == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input.lower() == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input.lower() == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tie!")
        draw +=1
    else:
        print("you lost!")
        computer_wins += 1
print("you won ", user_wins, "times.")
print("the computer won ", computer_wins, "times.")
print("number of ties", draw,"!")
print("good bye!")