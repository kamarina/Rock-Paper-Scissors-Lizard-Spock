import random
import time
import sys

"""
ideas & ways to improve:
-Get users to input their name and make the output more personalized
-add input validation

#TODO: 
Get mode selection question asked if user chooses 'y' to play another round
Mark user input in 2 player mode
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


def user_choice(prompt):
    while True:
        try:
            user = input(prompt).lower()

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
            return user_answer
        elif user_answer == "n":
            print("Goodbye!")
            break
        else:
            print("Please enter 'y' or 'n'.")


def single_player():
    user_win = 0
    comp_win = 0
    while True:
        user_result = user_choice("Please enter your choice: ")
        computer_result = computer_choice()
        index_user = GAME_LIST.index(user_result)
        index_comp = GAME_LIST.index(computer_result)
        while True:
            print("-" * 30)
            # try to use table
            #   YOU      |  COMPUTER
            # Spock 🖖  🆚  🤏 Lizard
            print(
                f"\nYou: {ITEMS_LIST[index_user]} - {SYMBOLS[index_user]}  🆚  {SYMBOLS[index_comp]} - "
                f"{ITEMS_LIST[index_comp]} :Computer")

            print("-" * 30)
            break

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

        continue_playing()

        # if not continue_playing():
        #     print("Goodbye 👋")
        #     break
        # else:
        #     return # return to mode selection

def two_players():
    player1_win = 0
    player2_win = 0
    while True:

        player1_result = user_choice("Player 1, enter your choice: ")
        player2_result = user_choice("Player 2, enter your choice: ")
        index_player1 = GAME_LIST.index(player1_result)
        index_player2 = GAME_LIST.index(player2_result)

        print("-" * 30)
        print(
            f"\nPlayer 1: {ITEMS_LIST[index_player1]} - {SYMBOLS[index_player1]}  🆚  {SYMBOLS[index_player2]} - "
            f"{ITEMS_LIST[index_player2]} :Player 2")

        print("-" * 30)
        break

    if player1_result == player2_result:
        print("It's a tie!")
        print(f"\nWin: {player1_win} \nLose: {player2_win}")
    elif (
            (player1_result == 'r' and (player2_result == 's' or player2_result == 'l')) or
            (player1_result == 's' and (player2_result == 'p' or player2_result == 'l')) or
            (player1_result == 'p' and (player2_result == 'r' or player2_result == 'k')) or
            (player1_result == 'l' and (player2_result == 'k' or player2_result == 'p')) or
            (player1_result == 'k' and (player2_result == 's' or player2_result == 'r'))
    ):
        print("Player 1 wins!!! ✨")
        player1_win += 1
        print(f"\nWin: {player1_win} \nLose: {player2_win}")
    else:
        print("Player 2 wins!!! ✨")
        player2_win += 1
        print(f"\nWin: {player1_win} \nLose: {player2_win}")

    continue_playing()
    # for i in user_choice():
    #     if not continue_playing():
    #         print("Goodbye 👋")
    #         break
    #     else:
    #         return

def play_game():
    while True:
        game_mode = input("Do you want to play Vs computer or another player? "
                        "\nType '1' to play against the computer, or '2' to play with a friend: ")
        if game_mode in("1", "2"):
            if game_mode == "1":
                single_player()
            elif game_mode == "2":
                two_players()
        else:
            print("Invalid choice, please enter '1' or '2'.")

game_menu()
play_game()
