import Flavors
import CoffeeMachineMenus as menu
import tabulate


class CoffeeMachine:
    COINS = [0.01, 0.05, 0.1, 0.25]

    def __init__(self, water=300, milk=200, cash=0, coffee=100):
        self._water = water
        self._milk = milk
        self._cash = cash
        self._coffee = coffee
        self._flavors = []

    @property
    def water(self):
        return self._water

    @property
    def milk(self):
        return self._milk

    @property
    def cash(self):
        return self._cash

    @property
    def flavors(self):
        return self._flavors

    @property
    def coffee(self):
        return self._coffee

    @water.setter
    def water(self, amount):
        self._water += amount

    @milk.setter
    def milk(self, amount):
        self._milk += amount

    @coffee.setter
    def coffee(self, amount):
        self._coffee += amount

    @cash.setter
    def cash(self, money):
        self._cash += money

    def report(self):
        """
        Return a detailed report with information about the amount of cash, water, milk  and coffee left in the Machine.
        :return: -> Report
        """
        # Emojis used
        milk = '\U0001f95b'
        report = '\U0001f4cb'
        water = '\U0001f4a7'
        cash = '\U0001f4b5'

        final_report = [
                [f"{milk}", "MILK AVAILABLE:", f"{self.milk} ml"],
                [f"{water}", "WATER AVAILABLE:", f"{self.water} ml"],
                [f"{menu.coffee}", "COFFEE AVAILABLE:", f"{self.coffee} g"],
                [f"{cash}", "CASH AVAILABLE:", f"$ {self.cash:.2f}"]
              ]
        title = f"{report} COFFEE MACHINE STATUS {report}\n"
        print(title.center(33))
        print(tabulate.tabulate(final_report, tablefmt='simple_grid', colalign=("center",)))

    def update(self):
        """
        Allow the user to manipulate the attributes of the Coffee Machine,
        providing a menu with one option for each attribute to be updated: --> Water-Milk-Coffee-Cash
        :return: None
        """

        save = '\U0001f4be'
        print(menu.config_menu)
        choice = menu.validate_choice(0, 1, 2, 3)
        # Water
        if choice == 0:
            ml = menu.validate_number("Enter the amount of water(ml) you want to charge > ")
            self._water += ml
        # Milk
        elif choice == 1:
            ml = menu.validate_number("Enter the amount of milk(ml) you want to charge > ")
            self._milk += ml
        # Cash
        elif choice == 2:
            money = menu.validate_number("Enter the amount of cash you want to charge: $ ")
            self._cash += money
        # Flavors
        else:
            flavors_existing = [name.name for name in self.flavors]
            while True:
                print(menu.flavor_menu)
                choice = menu.validate_choice(0, 1)
                if choice == 0:
                    Flavors.validate_flavor_info(self)
                else:
                    print(f"{save} Updated!")
                    break

    def get_coffee(self):
        """
        Provides a menu with all the flavors of coffee available in the machine,
        and pass the user's choice to the method 'prepare_order()' so it can use the resources available to prepare
        the order
        :return: None
        """

        # Emojis used
        coffee = '\u2615'
        chef = '\U0001f9d1\u200d\U0001f373'
        sad = '\U0001f61e'

        flavors = [flavor for flavor in self.flavors]
        list_flavor = tuple(order for order in range(len(flavors)))

        if flavors:
            print(f"{menu.report} MENU {menu.report}")
            for order, flavor in enumerate(flavors):
                print(f"{coffee} [{order}] - {flavor.name} | {menu.coin} {flavor.cost}")
            choice = menu.validate_choice(*list_flavor)
            order = flavors[choice]
            self.prepare_order(order)

        else:
            print(f"{sad} Sorry, we don't have any coffee to offer!")

    def prepare_order(self, order):
        """
        Receives a Flavor object as parameter and given the Flavor attributes, checks if the resources necessaries to
        make the drink are available and prepare the drink, return otherwise
        :return: None
        """

        # Emojis used
        coffee = '\u2615'
        chef = '\U0001f9d1\u200d\U0001f373'
        sad = '\U0001f61e'
        check = '\u2705'

        if order.ingredients['Water'] > self.water:
            print(f"{sad} Sorry, we ran out of water!")
            return
        elif order.ingredients['Milk'] > self.milk:
            print(f"{sad} Sorry, we ran out of milk!")
            return
        elif order.ingredients['Coffee'] > self.coffee:
            print(f"{sad} Sorry, we ran out of coffee!")
            return

        self.water = -order.ingredients['Water']
        self.milk = -order.ingredients['Milk']
        self.coffee = -order.ingredients['Coffee']

        payment = 0
        print(f"{menu.money} INSERT THE COINS | {order.name.upper()} COFFEE: $ {order.cost:.2f} {menu.money}")
        print(f"{menu.coin} [0] - $ 0.01\n{menu.coin} [1] - $ 0.05\n"
                f"{menu.coin} [2] - $ 0.10\n{menu.coin} [3] - $ 0.25")

        while True:
            money_left = order.cost - payment

            if money_left == 0:
                print(f"{check} PAYMENT ACCEPTED!")
                self.cash = payment
                break
            elif money_left < 0:
                if abs(money_left) > self.cash:
                    print(f"{menu.assistant} Sorry, we don't have enough money for your change!\n"
                          f"Here is your money back!")
                    return

                print(f"{check} PAYMENT ACCEPTED!")
                print(f"{menu.coin} HERE IS YOUR CHANGE $ {abs(money_left):.2f}")
                self.cash = payment - abs(money_left)
                break

            print(f"It is missing $ {money_left:.2f}")
            coins = menu.validate_choice(0, 1, 2, 3)
            payment += self.COINS[coins]

        print(f"{chef} CREATING A MASTERPIECE {chef}\n{coffee} Here is your {order.name}, enjoy! ")
        return
