import string
from helpers import alphabet_position, rotate_character   

def encrypt(text, key):
    message = ""
    index = 0
    for char in text:
        if char.isalpha():
            rot = alphabet_position(key[index % len(key)])
            message += rotate_character(char, rot)
            index += 1
        else:
            
            message += char
    return message 

def main():
    letter = input('enter a letter:')
    print(alphabet_position(letter))

    print(rotate_character('k', 7))

    key = (input("Please enter a code word: "))
    text = (input("Please enter a text: "))
    print(encrypt(text,key))

if __name__ == "__main__":
    main()        
