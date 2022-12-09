def binary_search(entered_list, item, index, low, high):
    #mostly done but some edge cases dont't work
    
    """ list must be orderd
    go to middle of list
    compare value to item
    if bigger ignore bigger half of list and vice bversa
    repeat until item is found or if item is not present
    output either index or true if item is present based on the value of index parameter
    or false if item is not present"""
    middle_index = (low + high)//2# finds the index of the middle value in the list
    print("lowest value", entered_list[low])# for testing print the lowest value of the range of the list being used
    print("middle value", entered_list[middle_index])# for testing print the midddle value
    print("highest value", entered_list[high])# for testing print the highest value of the range of the list being used
    print("item being searched for", item)
    if entered_list[middle_index] == item:# is middle val of list item
        print(f"i think it fails here, and this is the index of the search item {entered_list[middle_index]}")
        if index == True:# is index true
            print(middle_index)# if yes return and print index of middle value, which would be the earliest index of the item
            return middle_index
        elif index == False:
            print(True)# return and print True if item is in list
            return True
    elif entered_list[high] < item:#if search item is greater than largest value in list it is not there
        if index == True:# is index true
            return -1
        elif index == False:
            return False

            return False
    elif entered_list[middle_index + 1] == item:# copy of code above with variations so it checks the next value to so that if item is lats in list it doenst casue infinte loop
        print(f"i think it fails here, and this is the index of the search item {entered_list[middle_index]}")
        if index == True:# is index true
            print(middle_index + 1)# if yes return and print index of middle value + 1, which would be the earliest index of the item
            return middle_index + 1
        elif index == False:
            print(True)# return and print True if item is in list
            return True    
    elif low == high:# else return false  - if you get rid of this elif stuff it loops infintely
        if index == True:# is index true
            return -1
        elif index == False:
            return False
    elif item < middle_index + 1:# if item is less than middle value
        #recursive case
        bottom_list = entered_list[:middle_index]# botto half of list for testing
        print("bottom_list", bottom_list)# for testing prints section of list its currently using
        return binary_search(entered_list, item, index, low, middle_index)# call function with botto  half of list instead of total list
    elif item > middle_index - 1:# if item is greater than middle value
        # recursive case
        top_list = entered_list[middle_index:]# top half of list
        print("top_list", top_list)# test what the top half of the list is
        return binary_search(entered_list, item, index, middle_index, high)# call funcio again with top half of list
    
    



test_list = [1,2,3,4,5,6,7,8,10,11,12,13]# witho
print(f"index of search item is {binary_search(test_list, 9, True, 0, len(test_list)-1)}")