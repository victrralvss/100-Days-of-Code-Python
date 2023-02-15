import CoffeeMachineMenus as menu


def validate_flavor_info(machine):
    # Emojis used
    hungry = '\U0001f60b'
    cup_coffee = '\u2615'
    ingredients = '\U0001f374'
    pencil = '\u2712\ufe0f'

    # Flavors created
    flavors_created = [name.name for name in machine.flavors]
    print(f"{pencil} WRITING THE RECIPE {pencil}")
    while True:
        name = input(f"{cup_coffee} What is the drink's name: ").strip().title()
        if name in flavors_created:
            print("A flavor with this name already exists! Try another name")
            continue
        else:
            break

    print(f"{ingredients} ENTER THE RIGHT INGREDIENTS TO THE {name}")
    water = menu.validate_number(f"{menu.water} How much water (ml) goes in: ")
    milk = menu.validate_number(f"{menu.milk} How much milk (ml) goes in: ")
    coffee = menu.validate_number(f"{cup_coffee} How much coffee (g) goes in: ")
    cost = menu.validate_number(f"{menu.coin} How much {name} will cost: $ ")
    flavor = Flavor(name, {'Water': water, 'Milk': milk, 'Coffee': coffee}, cost)
    print(f"{menu.assistant}: Hmmm, I wonder what this is gonna taste like! {hungry}\n{'-' * 50}")
    machine.flavors.append(flavor)


class Flavor:
    def __init__(self, name, ingredients, cost):
        """
        Starts a new flavor of Coffee, with the given: Ingredients - Name - Cost
        """
        self._name = name
        self._ingredients = ingredients
        self._cost = cost

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def cost(self):
        return self._cost

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def set_cost(self):
        new_value = menu.validate_number("Enter the new value: $ ")
        self._cost = new_value

    def __str__(self):
        return f"{self.__class__.__name__} --> {' | '.join([f'{k}: {v}' for k,v in self.__dict__.items()])}"
