""" my attempt at making a merge sort
    this was coded on 01/05/2024

    PSEUDOCODE:

        take in list
        split list in half
        repeat previous step until every itme is in it's own list
        combine the list one by one e.g. list on right combine with list on left in pairs through all the list
        sort items when combining the lists
        repeat previous two steps until only one list of the original length is left
        list is now sorted

"""
# it doenst work
def my_merge(left_list, right_list):
    # list lengths
    right_list_length = len(right_list)
    left_list_length = len(left_list)

    # list indexes
    left_list_index = 0
    right_list_index = 0

    # final results/merged list
    merged_list = []

    while left_list_index < left_list_length and right_list_index < right_list_length:
        # if the next item in the left list is less than the next item in the right list, append it to the list
        if left_list[left_list_index] <= right_list[right_list_index]: 
            merged_list.append(left_list[left_list_index])
            # increment the index for the left list
            left_list_index += 1
        else:
            # else add the next itme in the right list to the final sorted list
            merged_list.append(right_list[right_list_index])
            # increment the right index
            right_list_index += 1

    # if ther are any values left in one of the list - only one will have items in it - append them to the end of the list
    merged_list.extend(left_list[left_list_index:])
    merged_list.extend(right_list[right_list_index:])

    return merged_list


def my_merge_sort(array_to_be_sorted):
    arr_length = len(array_to_be_sorted)
    if arr_length <= 1:
        return array_to_be_sorted
    else:
        middle_index = arr_length // 2
        left_list = my_merge_sort(array_to_be_sorted[:middle_index])
        right_list = my_merge_sort(array_to_be_sorted[middle_index:])

        return my_merge(left_list, right_list)

array_test = [1,2,3,2,4,5,78,92,5,64]

print(my_merge_sort(array_test))