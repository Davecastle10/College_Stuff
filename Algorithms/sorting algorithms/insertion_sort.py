""" My Attempt at making an insertion sort




    Pseudocode:

        Start with leftmost item,
        copy it into temp/current itme variable
        iterate through array, moving each item greater than the current itme 1 to the left, 
        until a smaller itme is found, 
        at which point the current itme is inserted at the index 1 to the left of the mslaller item
"""

def insertion_sort(arr_to_sort):
    for index in range(len(arr_to_sort)):
        current_item = arr_to_sort[index]
        new_index = index
        while new_index > 0 and arr_to_sort[new_index - 1] > current_item:
            arr_to_sort[new_index] = arr_to_sort[new_index - 1]
            new_index = new_index - 1
        arr_to_sort[new_index] = current_item
    return arr_to_sort

test_arr = [1,2,1,3,4,5,3,2,3,5,56467,6534,23,5,6,53,] 

print(insertion_sort(test_arr))
