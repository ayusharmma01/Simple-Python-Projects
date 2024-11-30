import random

def g_num(comp_choice):
    
    user_choice=int(input("Enter Your number between 1 to 100: "))
    if(user_choice > 100 ):
        print("please enter a valid number")
        return
    if comp_choice == user_choice:
        print("You guessed Right!!! Computer also thought ", comp_choice)
        return 1
    else: 
        if(comp_choice > user_choice):
            print("You chose lesser number than computer choice")
        else:
            print("You chose Greater number than computer choice")

        
        return 0
    

print("Guess the number game:  ")
comp_choice = random.randint(1, 100)
print(comp_choice)
res=0
for i in range (1,6): 
    
    res=g_num(comp_choice)
    if res == 1:
        break

    if i != 5:
        print("Remaining chances are: ",5-i)
        

if res == 0:
    print("Your chances are over!")
    