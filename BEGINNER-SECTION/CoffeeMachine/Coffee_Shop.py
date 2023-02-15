import CoffeeMachineMenus as menu
from Coffee_Machine import CoffeeMachine


def main():
    border = '-' * 50
    machine = CoffeeMachine()

    while True:
        print(border)
        print(menu.coffee_machine_menu)
        operation = menu.validate_choice("> ", 0, 1, 2, 3)

        if operation == 0:
            machine.report()
        elif operation == 1:
            machine.update()
        elif operation == 2:
            machine.get_coffee()
        else:
            print(f"{menu.assistant} Thanks for shopping with us!")
            return


if __name__ == "__main__":
    main()
