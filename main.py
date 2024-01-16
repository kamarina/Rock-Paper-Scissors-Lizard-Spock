import random
"""
ideas & ways to improve:
! Fix the new_game  'Would you like to play another round?' statement that is showing when the user is trying to run the program for the first time.

-display menu with the relevant options 
-Add 2-player mode so that 2 people can play against each other
-get input at the beginning to define if they want to play against the computer or a friend
-Get users to input their name and make the output more personalized
-run continuously until user prompts to exit
-add input validation
"""

def get_user_choice(): #  get user choice
    keep_going = True
    while keep_going:
        try:
            user_choice = input("Please enter your choice: 'r' for rock, 'p' for paper, 's' for scissors, "
                                "'l' for lizard, or 'sp' spock: ").lower()
            if user_choice not in ["r", "p", "s", "l", "sp"]:
                print("Invalid choice. Please enter 'r' for rock, 'p' for paper, 's' for scissors, "
                      "'l' for lizard, or 'sp' spock. ")
            else:
                keep_going = False
                return user_choice
        except KeyboardInterrupt:
            print("Input canceled by the user.")


def get_computer_choice():  # generate random choice for computer_choice variable
    return random.choice(["r", "p", "s", "l", "sp"])

def choices_explained(choice): #  this function is used in the final output, to explain the meaning of the dictionary's keys
    if choice == "s":
        return "for scissors"
    elif choice == "p":
        return "for paper"
    elif choice == "r":
        return "for rock"
    elif choice == "l":
        return "for lizard"
    else:
        return "for spock"


def winner(user_choice, computer_choice):  #  determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"

    outcomes = {
        ("r", "s"): "Rock crushes scissors!",
        ("s", "p"): "Scissors cut paper!",
        ("p", "r"): "Paper covers rock!",
        ("r", "l"): "Rock crushes lizard!",
        ("s", "l"): "Scissors decapitate lizard!",
        ("l", "p"): "Lizard eats paper!",
        ("l", "sp"): "Lizard poisons spock!",
        ("p", "sp"): "Paper disproves spock!",
        ("sp", "s"): "Spock smashes scissors!",
        ("sp", "r"): "Spock vaporizes rock!"
    }

    user_choice_str = str(user_choice)
    computer_choice_str = str(computer_choice)

    if (user_choice_str, computer_choice_str) in outcomes:
        return f"You won! {outcomes[(user_choice_str, computer_choice_str)]}"
    else:
        return f"Computer won! {outcomes[(computer_choice_str, user_choice_str)]}"


def play_game():  #  initiate a game
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose - {user_choice.upper()} {choices_explained(user_choice)}.")
    print(f"Computer chose {computer_choice.upper()} {choices_explained(computer_choice)}.")

    result = winner(user_choice, computer_choice)
    print(result)


new_game = input("Would you like to play another round? Type 'y' for Yes or 'n' for No.")  # ask the user if they would like to play another round
if new_game == "y":
    play_game()
else:
    print("We hope you enjoyed thr game!")

if __name__ == "__main__":
    play_game()
