print("\nWelcome to Rock Paper Scissors Game!!!")
print("\nYour Opponent is --> SYSTEM ")

import random

while True:
    user_choice = input("Enter your choice[rock:paper:scissors]: ")
    possible_response = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_response)
    print("\nYour response", user_choice)
    print("\nComputer response", computer_choice)

    if user_choice == computer_choice:
        print("\nBoth choices MATCH!!, ITS A TIE!!: ", user_choice, computer_choice)
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("\nPaper COVERS Rock, You LOSE!!!")
        elif computer_choice == "scissors":
            print("\n ROCK defeats SCISSORS!!, You WIN!!")
        elif computer_choice == "rock":
            print("\nIts a TIE, both obtain equal points")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("\nScissors CUTS THROUGH Paper, YOU lose")
        elif computer_choice == "rock":
            print("\nPaper COVERS Rock, You Advance!!")
        elif computer_choice == "paper":
            print("\n Its a TIE, both obtain equal points")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("\nScissors CUTS THROUGH Paper, You advance!!")
        elif computer_choice == "rock":
            print("\nSCISSORS Loses to ROCK, Computer ADVANCES!!")
        elif computer_choice == "scissors":
            print("\nIts a TIE, both obtain equal points")
    else:
        print("\nPLEASE enter proper choice")

    play_again = str(input("Do you want one more game? (y/n): "))
    if play_again.lower() != "y":
        break
