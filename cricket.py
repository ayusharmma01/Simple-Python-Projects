import random

# 1 means user has to bowl  and 0 means computer has to bowl
def bowling(turn, target):
    print("Bowling starts")
    sum = 0
    if turn == 1:
        print("Now you have to bowl and computer has to make ", target , " runs") 
    else:
        print("Now computer bowls and you have to make ", target) 

    while(turn == 0):
        comp_choice = random.randint(1,6)
        user_choice = get_valid_input("Enter number ranging 1 to 6: ")
        
        if(comp_choice == user_choice):
            print("Oops You are out at ",sum)
            return sum
        
        else:
            sum += user_choice
            print("Your total runs: ",sum)
            if(sum >= target):
                print("You won the game")
                return


    while(turn == 1):
        comp_choice = random.randint(1,6)
        user_choice = get_valid_input("Enter number ranging 1 to 6: ")
        if(comp_choice == user_choice):
            print("Wow! Computer gets out at ",sum)
            print("You Won!!!")
            return
        
        else:
            sum += comp_choice
            print("Computer's total runs: ",sum)   
            if(sum >= target):
                print("Computer won the game")
                return     
    

def batting(turn):
    sum = 0
    while(turn == 1):
        comp_choice = random.randint(1,6)
        user_choice = get_valid_input("Enter number ranging 1 to 6: ")
        
        if(comp_choice == user_choice):
            print("Oops You are out at ",sum)
            bowling(1, sum + 1)
            return
        else:
            sum += user_choice
            print("Your total runs: ",sum)

    while(turn == 0):
        comp_choice = random.randint(1,6)
        user_choice = get_valid_input("Enter number ranging 1 to 6: ")
        if(comp_choice == user_choice):
            print("Wow! Computer gets out at ",sum)
            bowling(0, sum + 1)
            return 
        else:
            sum += comp_choice
            print("Computer's total runs: ",sum)

def toss(user_input):
    comp_choice = random.randint(1,6)
    user = get_valid_input("Enter a number ranging 1 to 6: ")
    turn = -1
    print("Computer choice is: ", comp_choice)
    if ( ((comp_choice + user) % 2 == 0 and user_input == 1) or ((comp_choice + user) % 2 != 0 and user_input == 0) ):
        bat_bowl = get_valid_input("You won! Choose 1 to bat or 2 to bowl: ", 1, 2)
        res = "Congratulations, you have chosen to Bat" if bat_bowl == 1 else "Congratulations, you have chosen to Bowl"
        turn = 1 if bat_bowl == 1 else 0
        print(res)
    else:
        bat_bowl = random.randint(1,2)
        res = "Computer won and has chosen to Bat" if bat_bowl == 1 else "Computer won and has chosen to Bowl"
        turn = 0 if bat_bowl == 1 else 1
        print(res)

    batting(turn)
    

def even_odd():
    user_input = get_valid_input("Enter 1 for Even or 0 for Odd: ", 0, 1)
    if(user_input == 1):
        print("Your choice is Even")
    else:
        print("Your choice is Odd")
    print("Now it's time for the toss")
    toss(user_input)

def get_valid_input(prompt, min_value=1, max_value=6):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

even_odd()
