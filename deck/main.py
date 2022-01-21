import random


class Deck:
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    allCards = []

    def __init__(self):
        self.create()

    def __str__(self):
        return ', '.join(str(x) for x in self.allCards)

    def create(self):
        for i in self.cards:
            for j in self.suits:
                self.allCards.append(i + "-" + j)

    def shuffle(self):
        random.shuffle(self.allCards)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print(deck)
