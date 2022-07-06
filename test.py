from Card import Card
from Deck import Deck

mydeck = Deck()
mydeck.autoPopulate()
mydeck.shuffle()

for i in range(52):
    mydeck.dealOneCard()
