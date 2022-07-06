import random
from Card import Card

class Deck:
    def __init__(self):
        self.deck = []

    def autoPopulate(self):
        for rank in range(13):
            self.deck.append(Card(rank,"C"))
            self.deck.append(Card(rank,"D"))
            self.deck.append(Card(rank,"H"))
            self.deck.append(Card(rank,"S"))

    def viewDeck(self):
        for i in range(len(self.deck)):
            print(self.deck[i].getRank(), self.deck[i].getSuit())
        
    def addCard(self, Card):
        self.deck.append(Card)

    def dealOneCard(self):
        if len(self.deck) > 0:
            cardDealt = self.deck[-1]
            self.deck.pop()
            print("Dealt", cardDealt.getRank(), cardDealt.getSuit())
            return cardDealt
        else:
            print("Sorry, no more cards in deck =(")

    def shuffle(self):
        for currentCard in range(len(self.deck)-1, 0, -1):

            # Pick a random index from 0 to currentCard
            randomCard = random.randint(0, currentCard + 1)
        
            # Swap 'currentCard' with 'randomCard'
            self.deck[currentCard], self.deck[randomCard] = self.deck[randomCard], self.deck[currentCard]