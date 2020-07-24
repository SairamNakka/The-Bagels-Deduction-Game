import random
import time
def check(secretnumber,guess):
    if secretnumber==guess:
        return True
    else:
        return False
choice=3
def secret(choice):
    secretnum=""
    nums=list(range(10))
    random.shuffle(nums)#To choice a number with no repeating digits
    for i in range(choice):
        secretnum+=str(nums[i])
    return secretnum    
chance=1
while(chance!=0):
    secretnumber=int(secret(choice))
    #print(secretnumber)
    length=len(str(secretnumber))
    l=list(str(secretnumber))
    print("I am thinking of a",length,"digit number.Try to guess what it is.\nHere are some clues:\nWhen I say:")
    print("  Pico   -------> One digit is correct but in the wrong position.")
    print("  Fermi  -------> One digit is correct and in the right position.")
    print("  Bagels -------> No digit is correct.")
    print("You have 10 guesses to guess the number.")
    guesses=1
    while(guesses!=11):
        print("Guess #"+str(guesses))
        guess=int(input())
        guessnumber=list(str(guess))
        if len(guessnumber)>len(l) or len(guessnumber)<len(l):
            print("Invalid guess..")
            print("Please guess a",length,"digit number")
            continue
        guesses+=1    
        c=[]
        time.sleep(1)
        for i in range(len(guessnumber)):
            if guessnumber[i]==l[i]:
                c.append("Fermi")
            elif guessnumber[i] in l:
                c.append("Pico")
        if len(c)==0:
            print("Bagels")
            print("----------")
        else:
            for i in c:
                print(i,end=" ")
            print("\n---------")
        if check(secretnumber,guess)==True:
            chance=0
            print("You got it!!")
            break
    if check(secretnumber,guess)==False:
        chance=0
        print("Sorry, you ran out of guesses.The number was",secretnumber)
        break
    yes=["yes","y"]
    no=["no","n"]
    print("Do you want to play again? (yes/no)")            
    again=input()
    if again in yes:
        print("-------")
        chance=1
    else:
        chance=0
        print("Thanks for playing...Hope you have enjoyed!!")