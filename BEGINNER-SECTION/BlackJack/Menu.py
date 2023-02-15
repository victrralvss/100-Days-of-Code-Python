import emoji
import Players
import Deck


# Emojis used
bj_icon = emoji.emojize(':caça-níquel:', language='pt')
coin = emoji.emojize(':coin:')
play = emoji.emojize(':play_button:')
end = emoji.emojize(':cross_mark:')
dollar = emoji.emojize(':heavy_dollar_sign:')
flying_money = emoji.emojize(":money_with_wings:")
dice = emoji.emojize(":game_die:")


def valid(msg):
    while True:
        choice = input(msg).strip()
        if choice == str(0):
            return 0
        elif choice == str(1):
            return 1
        else:
            print("Please, enter a valid option!")


def initial_menu():
    """
    Displays the initial menu with all the information needed to start the game
    :return - Player
    """

    while True:
        # Initial Screen
        print(menu)
        choice = valid("YOUR ANSWER > ")
        if choice == 0:
            print("Thanks for playing!")
            return "game over"
        # Create the player and set the balance available to bet
        name = input("Type your name: ")
        player = Players.Dealer(name)
        player.set_balance()

        return player

def game_options(player, deck):
    """
    Displays the game options
    :return:
    """
    while True:
        print(options)
        print(f"{coin} YOUR BALANCE - $ {player._balance:.2f} | {emoji.emojize(':joker:')} DECK: {deck._size}")
        choice = valid("> ")
        if choice == 0:
            return 0
        elif choice == 1:
            return 1


# Menus to be displayed in the game
menu = f"{bj_icon} BLACKJACK {bj_icon}\nWelcome to BlackJack.py!, pick one option:\n1 - PLAY {play}\n0 - EXIT {end}"
options = f"{dollar} FEELING LUCKY TODAY? {dollar}\n[ 0 ] - CASH OUT {flying_money}\n[ 1 ] - DEAL {dice}"
