#Libraries
import random
#generaing the number
number = random.randint(1,100)
#Gameplay
guesses = []
print("Welcome to the number guesser, guess a number between 1 and 100, you have 5 turns")
turns = 5
while True:
    if turns!=0:
        try:
            guess = int(input(">"))
            if guess>100 or guess<1:
                print("Please enter a number between 1 and 100")
            else:
                if guess in guesses:
                    print("you already guesses this number")
                else:
                    if guess<number:
                        turns-=1
                        print(f"Guess Higher!, {turns} turns left")
                        guesses.append(guess)
                    elif guess>number:
                        turns-=1
                        print(f"Guess Lower, {turns} turns left")
                        guesses.append(guess)
                    else:
                        print("You guessed the number!")
                        break
        except TypeError:
            print("Enter an Integer please")
    else:
        print(f"You ran out of turns, the number was {number}")
        break
