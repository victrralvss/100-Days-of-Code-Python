from Coffee_Machine import CoffeeMachine
import Flavors

# Emojis used
coffee = '\u2615'
money = '\U0001f4b5'
coin = '\U0001fa99'
menu = '\U0001f9fe'
water = '\U0001f4a7'
report = '\U0001f4cb'
gear = '\u2699\ufe0f'
assistant = '\U0001f916'
milk = '\U0001f95b'
tools = '\U0001f6e0\ufe0f'
cup = '\U0001f9cb'
leave = '\u274c'


def validate_choice(*args, msg="> "):
    """
    Takes the options available for some operation and make sure the user enters a valid one
    :return: int -> The operation chosen
    """

    # Stores all the operations available
    ops = [arg for arg in args]
    while True:
        try:
            choice = int(input(msg).strip())
            if choice not in ops:
                raise AttributeError
            else:
                print(f"{tools} Working on that...")
                print('-'*50)
                return choice
        except (ValueError, AttributeError):
            print("Please, enter a valid option!")
            continue


def validate_number(msg):
    """
    Makes sure that all the number inputs sent to the machine performs some operation is valid
    :return: float
    """
    while True:
        try:
            choice = float(input(msg))
            if choice <= 0:
                raise ValueError
            else:
                return choice
        except ValueError:
            print("Please enter a valid number!")


title = f"{coffee} PYCOFFEE SHOP {coffee}\n"

# Coffee-Machine Menu
options = f"[0] - {report} REPORT\n[1] - {gear} UPDATE THE MACHINE\n[2] - {coffee} GET A COFFEE\n" \
          f"[3] - {leave} EXIT"
coffee_machine_menu = f"{title}{assistant}: Welcome to the Pycoffee Shop, what can I do for you?\n{options}"

# New flavor menu
flavor_menu = f"{title}[0] - {cup} NEW FLAVOR\n[1] - {leave} EXIT"

# Coffee's menu
coffee_menu = f""

# Coffee-Machine config menu
config_options = f"[0] - {water} UPDATE WATER STORAGE\n[1] - {milk} UPDATE MILK STORAGE\n" \
                 f"[2] - {money} UPDATE CASH STORAGE\n[3] - {menu} UPDATE MENU"
config_menu = f"{title}{assistant}: What do you want to update?\n{config_options}"
