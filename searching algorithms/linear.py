#returns true if the entered item is in the inputted list could be an array though

def linear_search(list, item, index):	
    """ parameters, the list, the item, and whether you want the index ( True) 
    or just to know if it's there (False) """
    for i in range(len(list)):
        if list[i] == item:
            if index == True:
                return i
            else:
                return True
    return False
    """  if you don't want to finish the function straight away use the 'pass' command 
    at the end of the function so it doesnt get excecuted"""

test_list = [1,2,3,4,5,23,45,9]

print(linear_search(test_list, 3, False))
print("index", linear_search(test_list, 3, True))
