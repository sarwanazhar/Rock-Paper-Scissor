import random

user_wins = 0
robot_wins = 0
option = ['rock', "paper", 'scissor']

while True:
    user_input = input(f"choose between rock paper scissor, or enter Q to exit: ").lower()
    if user_input == "q":
        break

    if user_input == option:
        continue

    
    random_number = random.randint(0,2)

    computer_pick = option[random_number]

    if user_input == "rock" and computer_pick == "rock":
        print(f"computer pick {computer_pick}. A DRAW")
    elif user_input == "rock" and computer_pick == "scissor":
        print(f"computer pick {computer_pick}. U WIN")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "paper":
        print(f"computer pick {computer_pick}. U LOSE")
        robot_wins += 1
    elif user_input == "paper" and computer_pick == "paper":
        print(f"computer pick {computer_pick}. A DRAW")
    elif user_input == "paper" and computer_pick == "scissor":
        print(f"computer pick {computer_pick}. A Lose")
        robot_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print(f"computer pick {computer_pick}. A WIN")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "rock":
        print(f"computer pick {computer_pick}. A LOSE")
        robot_wins += 1
    elif user_input == "scissor" and computer_pick == "scissor":
        print(f"computer pick {computer_pick}. A DRAW")
    elif user_input == "scissor" and computer_pick == "paper":
        print(f"computer pick {computer_pick}. A WIN")
        user_wins += 1

print(f'goodbye!. the score is robot = {robot_wins}, user = {user_wins}')