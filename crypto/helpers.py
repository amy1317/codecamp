import string

def alphabet_position(letter):
    letter = letter.lower()
    return list(string.ascii_lowercase).index(letter)

#print(alphabet_position(letter))

def rotate_character(char, rot):
    if (ord(char) >= 97) and (ord(char) <= 122): # lowercase
        return chr(97+(alphabet_position(char)+rot)%26)
    elif (ord(char) >= 65) and (ord(char) <=90): # uppercase
        return chr(65+(alphabet_position(char)+rot)%26)
    else:
        return char

