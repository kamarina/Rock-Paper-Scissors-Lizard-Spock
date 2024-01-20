import random
import time
import sys

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


def user_choice(player_name="Player 1"):
    while True:
        try:
            user = input(f"{player_name}, please choose: ").lower()
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
    while True:
        print("Welcome to Rock-Paper-Scissors-Lizard-Spock Game!")
        print("Select mode:")
        print("1. Play against the computer")
        print("2. Play against another player")
        mode = input("Enter your choice (1 or 2): ")

        if mode == "1":
            player_name = "Player"
            opponent_name = "Computer"
        elif mode == "2":
            player_name = "Player 1"
            opponent_name = "Player 2"
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        user_win = 0
        comp_win = 0
        while True:
            game_menu()
            user_result = user_choice(player_name)
            if mode == "2":
                game_menu()
                user_result_2 = user_choice("Player 2")
            else:
                user_result_2 = computer_choice()

            index_user = GAME_LIST.index(user_result)
            index_opponent = GAME_LIST.index(user_result_2)

            print("\033[34m-\033[0m" * 40)
            print(
                f"\n{player_name}: {ITEMS_LIST[index_user]} - {SYMBOLS[index_user]}  🆚  {SYMBOLS[index_opponent]} - {ITEMS_LIST[index_opponent]} :{opponent_name}")
            print("\033[34m-\033[0m" * 40)

            print(f"\033[33mRESULT: ", end="")

            if user_result == user_result_2:
                print("It's a tie!\033[0m")
                print(f"\n\033[32m{player_name} Win: {user_win} \n{opponent_name} Win: {comp_win}\033[0m")
                print("\033[34m-\033[0m" * 40)
            elif (
                    (user_result == 'r' and (user_result_2 == 's' or user_result_2 == 'l')) or
                    (user_result == 's' and (user_result_2 == 'p' or user_result_2 == 'l')) or
                    (user_result == 'p' and (user_result_2 == 'r' or user_result_2 == 'k')) or
                    (user_result == 'l' and (user_result_2 == 'k' or user_result_2 == 'p')) or
                    (user_result == 'k' and (user_result_2 == 's' or user_result_2 == 'r'))
            ):
                print(f"{player_name} wins!!! ✨\033[0m")
                user_win += 1
                print(f"\n\033[32m{player_name} Win: {user_win} \n{opponent_name} Win: {comp_win}\033[0m")
                print("\033[34m-\033[0m" * 40)
            else:
                print(f"{opponent_name} wins!!! 😑\033[0m")
                comp_win += 1
                print(f"\n\033[32m{player_name} Win: {user_win} \n{opponent_name} Win: {comp_win}\033[0m")
                print("\033[34m-\033[0m" * 40)

            if not continue_playing():
                print("Goodbye 👋")
                break

game()
