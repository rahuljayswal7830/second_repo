# number guessing game in python 
import random 
import os
import time

response="y"
while response=="y" or response=="Y":
    generated_by_computer=random.randint(1,20)
    user_response=[]
    number_of_attempt=5
    print("You have only 5 chance to guess the number ....\t".upper())

    while number_of_attempt>0:
        user_input=int(input("Enter a valid number from 1 to 20:= \t".upper()))
        print("\n")
        user_response.append(user_input)
        if user_input<1 or user_input>21:
            print("invalid number !!! Enter number between 1 to 20 \n".upper())
            time.sleep(2)
            os.system('clear')

        elif user_input>generated_by_computer:
            print("Value is too high...\n".upper())
            time.sleep(2)
            os.system('clear')

        elif user_input<generated_by_computer:
            print("Value is too low ...\n".upper())
            time.sleep(2)
            os.system('clear')
        elif user_input==generated_by_computer:
            break
        number_of_attempt-=1
        print(f"Remaining number of attempts := {number_of_attempt} \n".upper())
        time.sleep(2)
        os.system('clear')  


    if generated_by_computer in user_response:
        print(f"Well Done !!! You guessed the number {generated_by_computer}....\n".upper())
        time.sleep(2)
        os.system('clear')    
    else:
        print((f"oops !! Better luck next time ....\n").upper())
        time.sleep(2)
        os.system('clear')


    print(f"Computer generated number is {generated_by_computer} \n ".upper())
    print(f"Your  all inputs numbers:= {user_response} \n".upper())
    response=input("Do you want play again,Please enter (y/Y): \t".upper())
    print("\n")