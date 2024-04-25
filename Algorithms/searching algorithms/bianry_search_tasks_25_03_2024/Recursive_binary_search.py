""" This is an attempt at making a recursive binary search and assumes a sorted list is entered
"""

def recursive_binary_search(array_to_search, search_item):
    centre_index = int(len(array_to_search)/2)# centre index if odd or left of centre if eveen?
    if search_item == array_to_search[centre_index]:
        return True
    elif len(array_to_search) <= 1:
        return False

    elif search_item < array_to_search[centre_index]:
        return recursive_binary_search(array_to_search[:centre_index], search_item)
    
    elif search_item > array_to_search[centre_index]:
        return recursive_binary_search(array_to_search[centre_index:], search_item)
    


test_array = [1,2,3,4,5,6,7,8,9,10]
alpha_test_array = ["a", 'b', 'c', 'd']

print(recursive_binary_search(alpha_test_array, 'k'))


