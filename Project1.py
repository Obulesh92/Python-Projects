'''-------------------------Rock,Paper,Sessior---------------------------'''
#some basic game wining and losing rules given below:
''' 
    First_person    second_person       first_person win/lose

    rock            rock                ->Draw
    paper           paper               ->Draw
    sessior         sessior             ->Draw
    rock            paper               ->you lose
    rock            sessior             ->you win
    paper           sessior             ->you lose
    paper           rock                ->you win
    sessior         rock                ->you lose
    sessior         paper               ->you lose
'''

import random as rd 
#random module for second person

def Rock_paper_sessior(person):#Rock_paper_sessior is a function_name
    computer_choice=rd.randint(0,2)#computer_choice is for second person.
    print(f"computer choice  is {computer_choice}")

    if person == computer_choice:
        print("It is Draw")

    elif person==0:
        if computer_choice==2:
            return "You Win"

        else:
            return "You Lose"

    elif person==1:
        if computer_choice==0:
            return "You Win"

        else:
            return "You Lose"

    elif person==2:
        return "You Lose"

first_person=int(input("0 is rock,1 is paper,2 is sessior:"))

print(Rock_paper_sessior(first_person))#function call