import random
 
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")# The game rules

while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
    choice = int(input("User turn: "))#fetching the user inputs
    while choice > 3 or choice < 1:#varyfying if the user enters the exact choice 
        choice = int(input("enter valid input: "))# Now the user enters the choices
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print("user choice is: " +choice_name)
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print("Computer choice is: " + comp_choice_name)
    print(choice_name + " V/s " + comp_choice_name)
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("paper wins", end = "")
        result = "paper"
         
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("Rock win", end = "")
        result = "Rock"
    else:
        print("scissor wins", end = "")
        result = "scissor"
    if result == choice_name:
        print( ' ' + "<== User wins is==>")
    else:
        print("<== Computer wins ==>")
         
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N':
        break
print("\nThanks for playing")