import random
import time
import sys

"""
ideas & ways to improve:
! Fix the Would you like to play another round? statement that is showing when the user is trying to run the program for the first time 

-display menu with the relevant options 
-Add 2-player mode so that 2 people can play against each other
-get input at the beginning to define if they want to play against the computer or a friend
-Get users to input their name and make the output more personalized
-run continuously until user prompts to exit
-add input validation

#TODO: 
👊 rock 
✋ paper
✌️ scissors
🤏 lizard
🖖 Spock
"""

GAME_LIST = ["r", "p", "s", "l", "k"]
SYMBOLS = ["👊", "✋", "✌️", "🤏", "🖖"]
ITEMS_LIST = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
WIN = 0


def game_menu():
    print("-" * 50)
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock Game!")
    print("In this game, you can choose from the following options:")
    for i in range(len(GAME_LIST)):
        print(f"'{GAME_LIST[i]}' for {ITEMS_LIST[i]} - {SYMBOLS[i]}")


def user_choice():
    while True:
        try:
            user = input(": ").lower()
            if user in GAME_LIST:
                return user
            print("Please choose a valid option.")

        except KeyboardInterrupt:
            print("Interrupted!")
            break


def computer_choice():
    print("Computer is choosing... ")
    for _ in range(2):
        for symbol in SYMBOLS:
            sys.stdout.write(f"\r {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * len(SYMBOLS))
    sys.stdout.flush()
    random_choice = random.choice(GAME_LIST)
    index_list = GAME_LIST.index(random_choice)
    print(f"\nComputer choose {ITEMS_LIST[index_list]} - {SYMBOLS[index_list]}")
    return random_choice


def continue_playing():
    while True:
        user_answer = input("Do you want to play again? (y/n)").lower()
        if user_answer == "y":
            return True
        elif user_answer == "n":
            return False
        else:
            print("Please enter 'y' or 'n'.")


def game():
    user_win = 0
    comp_win = 0
    while True:
        game_menu()
        user_result = user_choice()
        computer_result = computer_choice()
        index_user = GAME_LIST.index(user_result)
        index_comp = GAME_LIST.index(computer_result)
        print("-" * 30)
        # try to use table
        #   YOU      |  COMPUTER
        # Spock 🖖  🆚  🤏 Lizard
        print(
            f"\nYou: {ITEMS_LIST[index_user]} - {SYMBOLS[index_user]}  🆚  {SYMBOLS[index_comp]} - {ITEMS_LIST[index_comp]} :Computer")

        print("-" * 30)

        if user_result == computer_result:
            print("It's a tie!")
            print(f"\nWin: {user_win} \nLose: {comp_win}")
        elif (
                (user_result == 'r' and (computer_result == 's' or computer_result == 'l')) or
                (user_result == 's' and (computer_result == 'p' or computer_result == 'l')) or
                (user_result == 'p' and (computer_result == 'r' or computer_result == 'k')) or
                (user_result == 'l' and (computer_result == 'k' or computer_result == 'p')) or
                (user_result == 'k' and (computer_result == 's' or computer_result == 'r'))
        ):
            print("You win!!! ✨")
            user_win += 1
            print(f"\nWin: {user_win} \nLose: {comp_win}")
        else:
            print("Computer win!!! 😑")
            comp_win += 1
            print(f"\nWin: {user_win} \nLose: {comp_win}")

        if not continue_playing():
            print("Goodbye 👋")
            break


game()
