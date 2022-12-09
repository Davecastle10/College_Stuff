# this doesn't work but is good for learning from mistakes


def binary_search(list, item, index):
    """ list must be orderd
    go to middle of list
    compare value to item
    if bigger ignore bigger half of list and vice bversa
    repeat until item is found or if item is not present
    output either index or true if item is present based on the value of index parameter
    or false if item is not present"""
    list_len = len(list)-1# length of list
    want_item = item
    bool_index = index

    midd_val  = int(list_len//2)# find middle value of list index
    bottom_list = list[:midd_val]# bottom half of list
    top_list = list[midd_val:]# top half of list
    if list[midd_val] == item:# if midlle value of list is the valut you are looking for
        if index == True:
            return midd_val# return the index of the item if the index parameter is true
        elif index == False:
            return True# return True if the item is present and the index parameter is false
    elif list[midd_val] > item:# if item is in bottom half of list, recursion with bottom_list
        binary_search(bottom_list, want_item, bool_index)
    elif list[midd_val] < item:# if item is in bottom half of list, recursion with top_list
        binary_search(top_list, want_item, bool_index)
    print(99)# check if it is looping
        
test_list = [1,2,3,4,5,9]
print(binary_search(test_list, 5, False))
