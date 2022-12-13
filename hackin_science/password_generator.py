""" this is my attempt at the hackin scinec password genertaor task, but it is only half done
"""



import random
def pwgen(length, with_digits, with_uppercase):
    pwd = ""# the password
    char_types = ["string"]# list fo char types used in password
    add_char_types = 0# index of what type of char in char types is being added to pwd
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alph_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [0,1,2,3,4,5,6,7,8,9]
    for i in range(length):
        if with_digits == True:
            char_types.append("digits")# add digits to char typoes list
        if with_uppercase == True:
            char_types.append("upps")# add upper case letter represtitve to char types list
        while len(pwd) < length:# while paswword has not reacxhed sdesired length
            if len(char_types) > 1:    
                add_char_types = random.rand(0,len(char_types))
            else:
                add_char_types = 0