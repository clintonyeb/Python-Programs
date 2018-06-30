# One object of this class represents black jacks, ranks, and suits.
class Card:
# this is a card constructer that constructs  a card each time it is called
    def __init__(self, rank, suit):
# Moved this up here so I can used them for my validations    
# This defines each cards' ranks in a special case dictionary
        self.ranks = dict([(1,"Ace"), (2,2), (3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10), (11, "Jack"),(12, "Queen"),(13, "King")])
# This defines my suits
        self.suits = {"s":"Spades","d":"Diamonds","c":"Clubs","h":"Hearts" }
# Let's verify the parameter passed to the __init__ function
        if(not isinstance(rank, int)):
          raise TypeError("Rank must be a number")
        if(not isinstance(suit, str)):
          raise TypeError("Suit must be a character")
        if(not (rank in self.ranks.keys())):
          raise ValueError("Rank must be a valid rank")
        if(not (suit in self.suits.keys())):
          raise ValueError("Suit must be a valid suit")
          
# This is where I define my variables
# This sets the value rank & suit to be passed on to the function as a parameter into class's instance variables
        self.rank = rank
        self.suit = suit
# These functions retrieve a rank, suit, bjValue of a card
    def getRank(self): # this method calls the rank value then return the value
        return self.rank
    def getSuit(self): # this method calls the suit value then return the value
        return self.suit
    def bjValue(self): # this method calls the Black Jack then return the value
        return self.rank
    # A function that covert objects to strings
    def __str__(self):
        return "%s of %s" % (self.ranks[self.rank], self.suits[self.suit])
    # [...] in self.suits[self.rank] indicates an array and I'm enabling the the return of value between 1-13
        
        # Stop using setData
        # The question is explicit when it says: "For this assignment, you will add code to the __init__() method that raises a:"
# def setData(self, rank, suit):
#     if rank <0 or rank<0:
#         raise ValueError()
#     self.rank = rank
#     self.suit = suit

                # Dont create objects like this!
# Card = Card() ## this is wrong
                # See how I do it, wish I can explain more..

try:
    # card.setData(-3,5)
    card = Card(-3, 5) # this automatically calls __init__ where we set

# Assignment for you: Learn how to print the message that was raise'd with the eror from __init__ instead of providing these fake messages.                    # the data and do the validations.
except ValueError:
    print("can't set Card to have zero number") # Is that the error you want to show
except TypeError:
    print ("can't set Card to have a negative number") # Check your error messages. If
                                                      # Not getting them ryt means you don'r prbably understand it.

c = Card(1, "s")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())

c = Card(2, "h")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())
"""Ace of Spades
1
s
1
2 of Hearts
2
h
2"""
