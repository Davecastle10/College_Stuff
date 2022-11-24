#returns true if the entered item is in the inputted list could be an array though

def search(list, item, index):	
    """ parameters, the list, the item, and whether you want the index ( True) 
    or just to know if it's there (False) """
    for i in range(len(list)):
        if list[i] == item:
            if index == True:
                return i
            else:
                return True
    return False

print(search([1,2,3,4,5], 3, False))