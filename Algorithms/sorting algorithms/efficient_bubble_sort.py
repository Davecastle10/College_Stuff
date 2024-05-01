""" This is an ascending bubble sort writtten to be more effciient than normal 
    or at least it should be pretty efficient if i did things right
    this was coded on 01/05/2024"""

def efficient_ascending_bubble_sort(array_to_be_sorted):
    end_pointer = len(array_to_be_sorted)
    sorted = False

    while sorted == False:
        sorted = True

        for i in range(end_pointer - 1):

            if array_to_be_sorted[i] > array_to_be_sorted[i + 1]:
                temp = array_to_be_sorted[i]
                array_to_be_sorted[i] = array_to_be_sorted[i + 1]
                array_to_be_sorted[i + 1] = temp
                sorted = False

        end_pointer = end_pointer - 1
    return array_to_be_sorted

test_array = [1,2,3,4,2,3,4,56,7,4,3,5,7,4,3,4,3,4,5,6,6,76,5,4,3]

print(efficient_ascending_bubble_sort(test_array))
