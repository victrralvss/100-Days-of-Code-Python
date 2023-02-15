import emoji
import Menu
from Deck import Deck
import Players


def main():
    def set_deck():
        """Set the deck and how much cards will be available in the game"""
        while True:
            create_deck = input(f"Do you wanna set the amount of cards in the deck? : Y - N\n> ").strip().lower()
            if create_deck == 'y':
                deck_cards = int(input("Set the amount of card you want to add in the deck MIN-60 and MAX-150\n> "))
                if deck_cards < 60 or deck_cards > 150:
                    print(
                        "The minimum amount of cards in the deck should be 60!\nThe default value of 100 will be used")
                    return Deck()
                else:
                    return Deck(deck_cards)
            elif create_deck == 'n':
                return Deck()
            else:
                print("Please, type a valid answer!")

    def betting(bet_money):
        stand_times = 0

        # Keep track of the money while the bet stills on
        total_bet = bet_money * 2

        # Stores the point of each player
        dealer_hand = 0
        house_hand = 0

        # Generate the cards used in the first round
        dealer_gen = deck.generate_cards(2)
        house_gen = deck.generate_cards(2)

        # Ends the game if the cards are over
        if dealer_gen == "over" or house_gen == "over":
            return None, None, None

        # Stores all the player's card
        dealer_cards = []
        house_cards = []

        stand = True
        hit = True

        while True:
            print(f"\n{'-' * 50}")

            if hit:
                dealer_cards = deck.displayCards(dealer_gen)
                dealer_hand = deck.get_hand_value(dealer_gen)

                if dealer_hand > 21:
                    return "bust", dealer_cards, dealer_hand
                elif dealer_hand == 21:
                    return "win", dealer_cards, dealer_hand

            if stand:
                if house_hand == 0:
                    house_cards = deck.displayCards(house_gen)
                    house_hand = deck.get_hand_value(house_gen)
                else:
                    print(f"HOUSE HAND: {' '.join(house_cards)} | POINTS: {house_hand}")
                    if dealer_hand == house_hand:
                        return "push", dealer_cards, dealer_hand

                    if abs(21 - dealer_hand) > abs(21 - house_hand):
                        return "bust", dealer_cards, dealer_hand
                    else:
                        return "win", dealer_cards, dealer_hand

            # Prints the players hand
            print(
                f"{emoji.emojize(':palm_up_hand:')} HOUSE HAND: {' '.join(house_cards[:-1])} | {emoji.emojize(':no_entry:')} ")
            print(f"{emoji.emojize(':palm_up_hand:')} YOUR HAND: {' '.join(dealer_cards)} | ")
            print(f"{emoji.emojize(':abacus:')} POINTS: {dealer_hand}")
            print(f"{emoji.emojize(':heavy_dollar_sign:')} BET: $ {total_bet:.2f}")
            print('-' * 50 + '\n')

            while True:
                keep = input(
                    f"{emoji.emojize(':collision:')} HIT or STAND {emoji.emojize(':raised_hand:')}\n> ").strip().lower()
                if keep == "hit":
                    dealer_gen.extend(deck.generate_cards())
                    stand_times += 1
                    stand = False
                    break
                elif keep == "stand":
                    house_gen.extend(deck.generate_cards(stand_times))
                    hit, stand = False, True
                    break
                else:
                    print("Please, type a valid answer!")

    # Set the player and the game's deck
    print('\n' + '-' * 50)
    dealer = Menu.initial_menu()
    if dealer == 'game over':
        return
    deck = set_deck()
    print('-' * 50 + '\n')

    while True:

        # Start the game
        action = Menu.game_options(dealer, deck)
        if action == 1:
            print('-' * 50 + '\n')
            bet = dealer.bet_value()

            game, game_hand, game_points = betting(bet)

            if game == "bust":
                print(f"BUST!\nYOUR HAND: {' '.join(game_hand)}\nYOUR POINTS: {game_points}")
                print(f"YOU WON: $ 0.00")
            elif game == "push":
                print(
                    f"PUSH!\nYOUR HAND: {' '.join(game_hand)}\nHOUSE POINTS: {game_points} YOUR POINTS: {game_points}")
                print(f"YOU WON: $ {bet:.2f}")
                dealer.balance = bet
            elif game == "win":
                print(f"YOU WIN!\nYOUR HAND: {' '.join(game_hand)}\nYOUR POINTS: {game_points}")
                print(f"YOU WON: $ {(bet * 2):.2f}")
                dealer.balance = (bet * 2)
                dealer.hands_won += 1
            else:
                print(f"{emoji.emojize(':trash:')} YOU RAN OUT OF CARDS \n")
                dealer.report()
                main()
            print('-' * 50 + '\n')

            if dealer.balance == 0:
                print(f"{emoji.emojize(':clown_face:')} YOU LOST EVERYTHING! GOOD LUCK IN THE NEXT ONE \n")
                dealer.report()
                main()
        else:
            dealer.report()
            main()


if __name__ == "__main__":
    main()
