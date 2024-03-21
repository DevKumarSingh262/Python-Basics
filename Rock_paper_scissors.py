import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock","paper","scissors"]:
        print("Invalid input")
        continue

#  Rock: 0 , paper: 1 , scissors: 2
 
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked:", computer_pick)

    if user_input == "rock" and computer_pick == 'scissors':
        print("You won")
        user_wins += 1
        continue

    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won")
        user_wins += 1
        continue

    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won")
        user_wins += 1
        continue

    elif user_input == 'rock' and computer_pick == 'rock':
        print("Draw")
        continue

    elif user_input == 'paper' and computer_pick == 'paper':
        print("Draw")
        continue

    elif user_input == 'scissors' and computer_pick == 'scissors':
        print("Draw")
        continue

    else:
        print("You Lost!")
        computer_wins += 1
        continue 

print ("you won", user_wins,"times")
print("The computer won", computer_wins,"times")
print("Goodbye!")
        