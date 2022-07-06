class Card:
    def __init__(self, rank, suit):
        self.ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.suits = {"C":"Clubs", "D":"Diamonds", "H":"Hearts", "S":"Spades"}
        
        self.rank = self.ranks[rank]
        self.suit = self.suits[suit]

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit