def encrypt(text, shift):
    new_text = ""
    max = len(alphabet) - 1
    shift = shift % max
    for letter in text:
        alph_index = alphabet.index(letter)
        if max - alph_index >= shift:
            new_text += alphabet[alph_index + shift]
        else:
            walk = alph_index + shift
            new_text += alphabet[(walk - max) - 1]

    return new_text

def decrypt(text, shift):
    new_text = ""
    max = len(alphabet)
    shift = shift % max
    print(shift)
    for letter in text:
        alph_index = alphabet.index(letter)
        new_text += alphabet[alph_index - shift]


    return new_text

def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower().strip().replace(' ', '')
        shift = int(input("Type the shift number:\n"))
        if direction == 'encode':
            ecrypted_word = encrypt(text, shift)
            print(ecrypted_word)
        elif direction == 'decode':
            decrypted_word = decrypt(text, shift)
            print(decrypted_word)



if __name__ == "__main__":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    main()