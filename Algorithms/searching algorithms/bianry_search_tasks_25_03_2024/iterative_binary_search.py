""" searches a sorted array via an iterative binary search

    This doesnt work!!!!!!!!!!!
"""


def iterative_binary_search(array_to_search, search_item):
    found = False
    found_index = -1 # base value so that if the item is not found it returns -1
    bottom_index_of_array = 0
    top_index_of_array = len(array_to_search) # this is actually the top index

    while found == False:
        centre_index = top_index_of_array - (top_index_of_array - bottom_index_of_array)//2# centre index
        if search_item == array_to_search[centre_index]:
            found_index = centre_index
            Found = True

        elif top_index_of_array - bottom_index_of_array == 0:
            found_index = -1 # technichally not needed as it should still be -1 from when the function was first called.
            found = True #ends the loop

        elif search_item < array_to_search[centre_index]:
            top_index_of_array = centre_index

        elif search_item > array_to_search[centre_index]:
            bottom_index_of_array = centre_index + 1

    return found_index
        
# bad bad bad bad bad bad 


test_array = [1,2,3,4,5,6,7,8,9,10]
alpha_test_array = ["a", 'b', 'c', 'd']

print(iterative_binary_search(test_array, 1))