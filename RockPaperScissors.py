import random

print("\nWelcome to Rock Paper Scissors Game!!!")
print("\nYour Opponent is --> SYSTEM ")

user_points = 0
system_points = 0
tie = 1

while True:
    user_choice = input("Enter your choice[rock:paper:scissors]: ")
    possible_response = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_response)
    print("\nYour response", user_choice)
    print("\nComputer response", computer_choice)

    try:
        if user_choice == "rock":
            if computer_choice == "paper":
                print("\nPaper COVERS Rock, You LOSE, SYSTEM WINS!!!")
                system_points += 1
                print("\nSYSTEM's score is: ", system_points)

            elif computer_choice == "scissors":
                print("\n ROCK defeats SCISSORS!!, You WIN!!")
                user_points += 1
                print("\nUSER's score is: ", user_points)

            elif computer_choice == "rock":
                print("\nIts a TIE, both obtain equal points")
                tie += 1
                print("\nScores are LEVEL", tie)

            elif user_choice == "paper":
                if computer_choice == "scissors":
                    print("\nScissors CUTS THROUGH Paper, SYSTEM WINS, YOU lose")
                    system_points += 1
                    print("\nSYSTEM's score is: ", system_points)

            elif computer_choice == "rock":
                print("\nPaper COVERS Rock, You WIN!!")
                user_points += 1
                print("\nUSER's score is: ", user_points)

            elif computer_choice == "paper":
                print("\n Its a TIE, both obtain equal points")
                tie += 1
                print("\nScores are LEVEL", tie)

            elif user_choice == "scissors":
                if computer_choice == "paper":
                    print("\nScissors CUTS THROUGH Paper, You ADVANCE!!")
                    user_points += 1
                    print("\nUSER's score is: ", user_points)

            elif computer_choice == "rock":
                print("\nSCISSORS Loses to ROCK, Computer ADVANCES!!")
                system_points += 1
                print("\nSYSTEM's score is: ", system_points)

            elif computer_choice == "scissors":
                print("\nIts a TIE, both obtain equal points")
                tie += 1
                print("\nScores are LEVEL", tie)
                print(f"\nUSER's score.{user_points}: "
                      f"\nand SYSTEM's score.{system_points}: ")
            else:
                print("\nPLEASE enter proper choice")

        print(f"FINAL SCORES ARE; USER: {user_points} and SYSTEM: {system_points}")

        play_again = str(input("Do you want one more game? (y/n): "))
        if play_again.lower() != "y":
            break

    except ValueError as e:
        print(e)
        print("enter valid input rock/paper/scissor")
