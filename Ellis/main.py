# object of the class Card stores data i.e. ranks, suit, face up cards, black jack values
class Card:
    # constructs a card each time a card is called
    def __init__(self, rank, suit):
      # Requred variables
        self.ranks = dict([(1, "Ace"), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, "Jack"), (12, "Queen"), (13, "King")])
        self.suits = {"d":"Diamonds", "s":"Spades", "c":"Clubs", "h":"Hearts" }
        self.rank = rank
        self.suit = suit
      
    def bjValue(self):
        return self.rank

    def getRank(self):
        return self.rank
        
    def getSuit(self):
        return self.suit
        
# this function covert objects to strings
    def __str__(self):
        # return "%s of %s" % (self.rank[self.rank], self.suit[self.suit], self.BJValue())
        return "%s of %s" % (self.ranks[self.rank], self.suits[self.suit])
        # return ("%s of %s" % (Ace, Spade)
  
## This is what I need to input to get#####
c = Card(1, "s")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())

# #### DESIRED OUTPUT #####
# Ace of Spades
# 1
# s
# 1

## More Tests
c = Card(2, "d")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())

# #### DESIRED OUTPUT #####
# 2 of Diamonds
# 2
# d
# 2

c = Card(13, "h")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())

# #### DESIRED OUTPUT #####
# King of Hearts
# 13
# h
# 13