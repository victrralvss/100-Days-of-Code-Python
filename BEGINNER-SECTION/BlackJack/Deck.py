import random
import emoji


class Deck:
    """
    Starts a deck, with the number of cards given, if the number is not informed, creates a deck with 100 cards
    """
    ranks = {"hearts": 9829, "diamonds": 9830, "spades": 9824, "clubs": 9827, }
    cards = {'A': 11, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, size=100):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self):
        self._size -= 1

    def generate_cards(self, amount=1):
        """
        Given the amount of cards to create, returns a random list containing the card's RANK and VALUE,
        which can be used as a key to get their values in the game in a dict
        :param amount: int - Number of cards to create
        :return: list - The rank and value of each card
        """
        create = {}

        while amount:
            rank = random.choice(list(self.ranks.keys()))
            card = random.choice(list(self.cards.keys()))
            password = rank + str(card)

            if create.get(password):
                continue
            else:
                create.update({password: [rank, card]})
                self._size -= 1
                amount -= 1

        if self._size == 0:
            print("YOU RAN OUT OF CARDS!")
            return "over"

        return list(create.values())

    def display_cards(self, cards: list):
        """Display the cards in your hand"""
        hand = []
        for card in cards:
            rank, value = card
            hand.append(f"{emoji.emojize(':joker:', variant='emoji')} - {value}{chr(self.ranks[rank])}")

        return hand

    def get_hand_value(self, hand):
        value = 0
        as_in_hand = 0

        for card in hand:
            value += self.cards[card[1]]
            if card[1] == 'A':
                as_in_hand += 1

        if as_in_hand == 1 and value > 21:
            value -= 10
        elif as_in_hand > 1:
            value -= 10 * (as_in_hand - 1)
            if value > 21:
                value -= 10

        return value

