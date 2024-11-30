import random

def game():
    print("Welcome to the game!!")
    print()

    choice = random.randint(1,3)

    myDict = {
        1 : "Stone",
        2 : "Paper",
        3 : "Scissor", 
    }

    print("Your choices are :- ")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissor")

    user_choice = int(input('Enter your choice (1, 2 or 3 ):- '))

    if choice != user_choice :
        print("You won!!!!!  Computer selected ",myDict[choice])
    else :
        print("You Lost")


mann = 1

while mann == 1:
    game()
    mann_input = int(input(("Do you want to play again ?? ( 1 -> Yes & 0 -> No ) ")))
    if mann_input == 1:
        mann = 1
    else:
        mann = 0
        print("Thanks for playing the game.")
        break
    