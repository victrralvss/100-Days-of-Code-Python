import gameRules
import gameMenu


def main():
    # Emojis used
    battle = '\u2694\ufe0f'
    trophy = '\U0001f3c6'

    # Keeps track of the player's performance, while True, the game stills on
    winning = True
    score = 0

    # Stores the people being compared
    person_a = {}
    person_b = {}

    while winning:
        print('-'*50)
        print(gameMenu.game_menu)

        # Set the initial comparison
        if score == 0:
            while True:
                person_a = gameRules.get_person()
                person_b = gameRules.get_person()
                if person_b is not person_a:
                    break

        # Swap the first person with the second one and gets a new one to compare
        else:
            while True:
                person_a, person_b = person_b, gameRules.get_person()
                if person_a is not person_b:
                    break

        print(f"(A) {person_a['name']}, a {person_a['description']}, from {person_a['country']}\n{battle}")
        print(f"(B) {person_b['name']}, a {person_b['description']}, from {person_b['country']}?")


        while True:
            guess = input(f"> ").lower().strip()
            if guess == 'a':
                winning = gameRules.who_has_followers(person_a, person_b)
                print('-' * 50)
                break
            elif guess == 'b':
                winning = gameRules.who_has_followers(person_b, person_a)
                print('-' * 50)
                break
            else:
                print("Please type a valid answer!")
                continue

        if winning:
            score += 1
        else:
            print(f"{trophy} YOUR SCORE: {score}")
            break

    while True:
        keep_playing = input(f"\U0001f575\ufe0f WANNA PLAY AGAIN? [Y] - [N]\n> ").lower().strip()
        if keep_playing == 'y':
            main()
        elif keep_playing == 'n':
            print("THANKS FOR PLAYING!")
            return
        else:
            print("Please type a valid answer!")


if __name__ == "__main__":
    main()

