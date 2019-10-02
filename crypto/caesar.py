import string
from helpers import alphabet_position, rotate_character   

def encrypt(text, rot):
    encrypted = ""
    for i in list(text):
        encrypted += rotate_character(i, rot)
    return encrypted

                                                                                   
def main():
    # your main code (input and print statements)
    letter = input('Type a message:')
    print(encrypt(letter, 5))

if __name__ == "__main__":
    main()        


