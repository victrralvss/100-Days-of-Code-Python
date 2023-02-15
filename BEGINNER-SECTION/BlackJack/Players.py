import emoji
import tabulate

class Dealer:
    """The player(s) who is betting against the house"""

    def __init__(self, name):
        self._name = name
        self._balance = 0
        self._bet = 0
        self._hands_won = 0

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    @property
    def bet(self):
        return self._bet

    @property
    def hands_won(self):
        return self._hands_won

    @hands_won.setter
    def hands_won(self, amount):
        self._hands_won += amount

    @balance.setter
    def balance(self, amount):
        """
        Set the initial player's balance with the amount given, it can only be used when the game starts.
        :return: None
        """
        self._balance += amount

    def bet_value(self):
        """

        :return: float - Amount of money bet
        """
        # Emojis used
        coin = emoji.emojize(":coin:")
        money = emoji.emojize(":money_bag:")
        flying_money = emoji.emojize(":money_with_wings:")

        print(f"{money} PLACE YOUR BET {money}\n{coin} CURRENT BALANCE: $ {self._balance:.2f}")
        while True:
            try:
                bet = float(input("> $ "))
            except ValueError:
                print("Please enter a valid amount of money!")
                continue

            if bet > self._balance or bet == 0:
                print(f"You don't have enough money to bet!{flying_money}")
            else:
                self._balance -= bet
                self._bet += bet
                print("Get ready!")
                return bet

    def set_balance(self):
        while True:
            money = input("How much money do you want put in this game: $ ")
            if money.isdigit() and float(money) >= 10:
                self._balance = float(money)
                print("Balance updated!")
                return
            else:
                print("Please enter a valid number greater or equal $10,00")

    def report(self):
        """
        Prints a report with a short description about the user's performance in the game,
        the following information are given: Total bet - Profit - Hands won - Final Balance
        :return: str
        """
        # Emojis used
        medal = emoji.emojize(':1st_place_medal:')
        money_bag = emoji.emojize(':money_bag:')
        suitcase = emoji.emojize(':briefcase:')
        player = emoji.emojize(':saluting_face:')
        scores = [
                    [f"{player} ", "PLAYER", f"{self.name}"],
                    [f"{medal} ", "HANDS WON", f"{self.hands_won}"],
                    [f"{money_bag} ", "PROFIT", f"$ {(self.balance - self.bet):.2f}"],
                    [f"{suitcase} ", "FINAL BALANCE", f"$ {self.balance:.2f}"],
                  ]
        trophy = emoji.emojize(":trophy:")
        print(f"{f'{trophy} YOUR SCORE {trophy}'.center(25, ' ')}")
        print(tabulate.tabulate(scores))

