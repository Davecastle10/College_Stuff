def binary_search(list, item, index):
    """ list must be orderd
    go to middle of list
    compare value to item
    if bigger ignore bigger half of list and vice bversa
    repeat until item is found or if item is not present
    output either index or true if item is present based on the value of index parameter
    or false if item is not present"""
    middle_value = (len(list)-1)//2# finds the index of the middle value in the list
    print(middle_value)
    if list[middle_value] == item:# is middle val of list item
        if index == True:# is index true
            return middle_value# if yes return index of middle value
        elif index == False:
            return True# return True if item is in list
    elif item < middle_value:# if itme is less than middle value
        bottom_list = list[:middle_value]# botto half of list
        binary_search(bottom_list, item, index)# call function with botto  half of list instead of total list
    elif item > middle_value:# if item is greater than middle value
        top_list = list[middle_value:]# top half of list
        print(top_list)# test what the top half of the list is
        binary_search(top_list, item, index)# call funcio again with top half of list
    else:# else return false
        return False
    



test_list = [1,2,3,4,5,9,100,123,1234,12345, 999999999, 999999999999]# witho
print(binary_search(test_list, 5, False))