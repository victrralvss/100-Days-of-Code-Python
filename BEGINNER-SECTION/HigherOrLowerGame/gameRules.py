from gameData import data
import random


def get_person():
    """
    Search for a random person in the data, and return a dict with the person's information, such as:
    name - description - instagram followers - Country
    :return: Dict
    """
    return random.choice(data)

def who_has_followers(guess, compared):
    """
    Takes the number of followers on Instagram from two persons and compare them,
    if the chosen person has more followers return True, False otherwise
    :param chosen: int
    :param compared: int
    :return: Boolean
    """

    # Emojis used
    red = '\U0001f534'
    green = '\U0001f7e2'
    star = '\u2b50'
    bomb = '\U0001f4a3'

    if guess['follower_count'] > compared['follower_count']:
        print(f"{star} Nice!\n{green} {guess['name']} has {guess['follower_count']}M followers")
        print(f"{red} {compared['name']} has {compared['follower_count']}M followers")
        return True
    elif guess['follower_count'] < compared['follower_count']:
        print(f"{bomb} Ops!\n{red} {compared['name']} has {compared['follower_count']}M followers")
        print(f"{green} {guess['name']} has {guess['follower_count']}M followers")
        return False
    else:
        print(f"{star} Nice!\n{green} {guess['name']} has {guess['follower_count']}M followers")
        print(f"{red}  {compared['name']} has {compared['follower_count']}M followers")
        return True


