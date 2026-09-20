#Libraries
import random
from random_word import RandomWords

#Getting Random Word
wordClass = RandomWords()
word = wordClass.get_random_word()

#storing correct guesses and wrong guesses
correct_guess = []
wrong_guess = []
#giving user a hint
vowels = ['a','e','i','o','u']
vowel_count = 0
for letter in word:
    if letter in vowels:
        vowel_count+=1
turns =int(len(word) + 3)
print(f"The word has {vowel_count} vowels")
#User guess loop
while turns>0:
    print(f"You have {turns} turns left")
    for letter in word:
        if letter in correct_guess:
            print(f"{letter}",end="")
        else:
            print("_",end="")
    flag = True
    for letter in word:
            if letter not in correct_guess:
                flag = False
    if flag:
        print("\nCongratulations, You Won!")
        break
    guess = input("\nEnter guess :")
    if len(guess)!=1:
        print("please enter a single letter")
    else:
        if guess in wrong_guess:
            print("You already guessed this letter")
        else:
            for letter in word:
                if letter==guess:
                    correct_guess.append(guess)
                else:
                    wrong_guess.append(guess)
            turns-=1
if turns==0:
    print(f"You lost :( \nthe word was {word}")



    

