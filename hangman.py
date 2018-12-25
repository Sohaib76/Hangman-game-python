import random
import os
 
def select(word,guesses,guess):
    status = ''
    match=0
    broj=0
    for letter in word:
        if letter in guesses:
            status+=letter+" "
        else:
            status+="_ "
        if letter==guess:
            match+=1
 
    if match>0:print("Bravo you guessed a letter!")
    else:
        print("You did not hit the letter")
        broj += 1
    return [status,broj]
 
hangman=[
"""
______
|    
|    
|    
|
|
|
""",
"""
______
|     |
|    
|    
|
|
|
""" ,
"""
______
|     |
|     O
|    
|
|
|
""" ,
"""
______
|     |
|     O
|     |
|
|
|
""" ,
"""
______
|     |
|     O
|    /|
|
|
|
""" ,
"""
______
|     |
|     O
|    /|\
|
|
|
""" ,
"""
______
|     |
|     O
|    /|\
|    /
|
|
""" ,
"""
______
|     |
|     O
|    /|\
|    / \
|
|
"""
]
 
 
def get_word():
    words=["jabuka","mandarina","bostan","paprika","krompir","paradajz","masline","jagoda"]
    return random.choice(words).upper()
 
def main():
    guesses=[]
    guessed=False
    word=get_word()
    num_guess=7
    print("WELCOME TO HANGMAN ULTIMATE!\n You have, ",num_guess ," attempt.")
    while ( not guessed  and num_guess>0):
        print(hangman[7 - num_guess])
        print("Write a Letter!")
        guess=input().upper()
        if len(guess)== len(word):
            guesses.append(guess)
            if guess==word:
                guessed=True
            else:
                num_guess-=1
                print("You did not hit the rec! Number of trials: ",num_guess)
 
        elif guess in guesses:
            print("A Word ",guess," you've already tried.")
        elif len(guess)==1:
            guesses.append(guess)
            result=select(word,guesses,guess)
            if result[0].replace(" ","") ==word:
                guessed=True
            else:
                num_guess-=result[1]
                print("The rest is you ",num_guess," attempt.")
                print(result[0])
        else:
            print("Improper input.")
 
 
    if num_guess >0:
        print("Bravo! You missed the word ",word,"Number of trials: ",len(guesses))
    else:
        print("You've used all the tests. "," Rec was: ",word)
 
    os.system("cls")
main()
