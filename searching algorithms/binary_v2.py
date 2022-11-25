def binary_search(entered_list, item, index, low, high):
    """ list must be orderd
    go to middle of list
    compare value to item
    if bigger ignore bigger half of list and vice bversa
    repeat until item is found or if item is not present
    output either index or true if item is present based on the value of index parameter
    or false if item is not present"""
    middle_value = (low + high - 1)//2# finds the index of the middle value in the list
    print("lowest value", entered_list[low])# for testing print the lowest value of the range of the list being used
    print("middle value", entered_list[middle_value])# for testing print the midddle value
    print("highest value", entered_list[high])# for testing print the highest value of the range of the list being used
    print("item being searched for", item)
    if entered_list[middle_value] == item:# is middle val of list item
        if index == True:# is index true
            print(middle_value)# if yes return and print index of middle value, which would be the earliest index of the item
            return middle_value
        elif index == False:
            print(True)# return and print True if item is in list
            return True
    elif low == middle_value:# else return false
        return False
        print(False)
    elif item < middle_value:# if item is less than middle value
        bottom_list = entered_list[:middle_value]# botto half of list for testing
        print("bottom_list", bottom_list)# for testing prints section of list its currently using
        binary_search(entered_list, item, index, low, middle_value)# call function with botto  half of list instead of total list
    elif item > middle_value:# if item is greater than middle value
        top_list = entered_list[middle_value:]# top half of list
        print("top_list", top_list)# test what the top half of the list is
        binary_search(entered_list, item, index, middle_value, high)# call funcio again with top half of list
    
    



test_list = [1,2,3,4,5,9,100,123,1234,12345]# witho
print(binary_search(test_list, 9, False, 0, len(test_list)-1))