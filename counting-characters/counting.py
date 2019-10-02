string_1 = ("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut 
 ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat.
 Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat 
 eget massa. Donec nec velit non ligula efficitur luctus.""")

test_str = {}
for i in string_1: 
    if i in test_str: 
        test_str[i] += 1
    else: 
        test_str[i] = 1

for akey in test_str.keys():     
    print(akey, '',test_str[akey])
    