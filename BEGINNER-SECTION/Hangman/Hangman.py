from random import choice
import emoji


def main():
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = choice(word_list)
    guess_word = ["_" for _ in chosen_word]
    used_letters = set()
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    users_life = len(stages)
    tries = 0
    print(f"{' HANGMAN '.center(40, '°')}")

    def get_letter():
        while True:
            guess = input("Guess a letter... > ").strip().lower()
            if guess in used_letters:
                print("Try another word, this one has already been used!")
                continue
            if guess.isalpha() and len(guess) == 1:
                return guess
            else:
                print("Please enter only one alphabetic letter!")

    while True:
        print(stages[users_life - 1 - tries])
        print(f"{emoji.emojize(':red_heart:', variant='emoji_type') * (users_life - (tries + 1))}")
        print(f"WORD:\t{' '.join(guess_word)}")

        guess = get_letter()
        used_letters.update(guess)
        print(f"\n{''.center(40, '°')}")

        for i, word in enumerate(chosen_word):
            if guess == word:
                guess_word[i] = guess

        if guess not in chosen_word:
            tries += 1

        if tries == users_life - 1:
            print(emoji.emojize(":lápide:", language="pt"), "YOU LOSE!")
            print(f"The word was {chosen_word}")
            break

        elif chosen_word == ''.join(guess_word):
            print(emoji.emojize(":trophy:"), "CONGRATULATIONS, YOU WIN!")
            print(f"The word was {chosen_word}")
            break

    if input("Thank's for playing! Do you wanna play again? Y - N\n> ").lower() == "y":
       main()
    else:
        return

if __name__ == "__main__":
    main()
