#Libraries 
import random
#Lists & variables
cards = ['A','K','Q','J',10,9,8,7,6,5,4,3,2]
playerCards = []
dealerCards = []
playerValue = 0
dealerValue = 0
playerAceCount = 0
dealerAceCount = 0
playerBust = False
dealerBust = False
playerStand = False
#Functions
def hit(player):
    global cards,playerAceCount,playerValue,dealerAceCount,dealerCards,dealerValue,playerCards
    card = random.choice(cards)
    if player == "p":
        playerCards.append(card)
        if card in ['K','Q','J']:
            playerValue+=10
        elif card == "A":
            playerAceCount+=1
            playerValue+=11
        else:
            playerValue+=card
    if player == "d":
            dealerCards.append(card)
            if card in ['K','Q','J']:
                dealerValue+=10
            elif card == "A":
                dealerAceCount+=1
                dealerValue+=11
            else:
                dealerValue+=card
def bust(player):
    global playerAceCount,playerValue,dealerAceCount,dealerValue,playerBust,dealerBust
    if player == "p":
        if playerValue>21:
            if playerAceCount!=0:
                playerValue-=10
                playerAceCount-=1
            else:
                playerBust = True
    if player == "d":
        if dealerValue>21:
            if dealerAceCount!=0:
                dealerValue-=10
                dealerAceCount-=1
            else:
                dealerBust = True
#dealing cards
for deal in range(2):
    hit("p")
    hit("d")
#gameplay
while True:
    print(f"Dealer : {dealerCards[0]}\nPlayer : {playerCards}")
    bust(player="p")
    bust(player="d")
    if playerBust==True:
        print(f"Player Busted")
        break
    else:
        choice = input("hit or stand?\n")
        if choice == 'hit':
            hit(player="p")
        else:
            playerStand = True
            break
if playerStand:
    print(f"Dealer : {dealerCards}\nPlayer : {playerCards}")
    if dealerValue>21:
        print("Dealer busted")
    while dealerValue<17:
        hit("d")
        print(f"Dealer : {dealerCards}\nPlayer : {playerCards}")
        bust("d")
        if dealerBust:
            print("Dealer busted! Player won!")
            break
    if dealerBust!=True:
        if playerValue>dealerValue:
            print("player Won")
        elif playerValue==dealerValue:
            print("Draw")
        else:
            print("Dealer Won")