def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    
    new_list = fullname.split()
    
    initials = ""

    for name in new_list:  
        initials += name[0].upper()  

    return initials

def main():
    name_initials = input("What is your full name?")
    print(get_initials(name_initials))
    
if __name__ == '__main__':
    main()



