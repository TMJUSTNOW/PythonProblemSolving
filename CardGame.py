import random

class Number(object):
  ACE = 1
  TWO = 2
  JACK = 11
  QUEEN = 12
  KING = 13

  @staticmethod
  def ToString(num):
    if num == 1:
      return "A"
    elif num <= 10:
      return str(num)
    elif num == 11:
      return "J"
    elif num == 12:
      return "Q"
    else:
      return "K"

class Suit(object):
  HEART = 1
  DIAMOND = 2
  CLUB = 3
  SPADE = 4

  @staticmethod
  def ToString(suit):
    if suit == 1:
      return u"\u2665"
    elif suit == 2:
      return u"\u2666"
    elif suit == 3:
      return u"\u2663"
    else:
      return u"\u2660"

class Card(object):
  def __init__(self,num,suit):
    self.suit = suit
    self.num = num

  def printCard(self):
    print self.ToString()

  def ToString(self):
    return Suit.ToString(self.suit) + Number.ToString(self.num)

class Deck(object):
  def __init__(self):
    self.allCards = [Card(i,j) for i in range(1,14) for j in range(1,5)]
  # Fisher-Yates shuffle
  def shuffle(self):   
    for i in range(len(self.allCards)-1,-1,-1):
      j = random.randint(0,i+1)
      temp =self.allCards[i] 
      self.allCards[i] = self.allCards[j] 
      self.allCards[j] = temp

  def deal(self):
    return self.allCards.pop()
  def printDeck(self):
    for card in self.allCards:
      card.printCard()
deck = Deck()
deck.shuffle()
deck.printDeck()
card = deck.deal()
card.printCard()