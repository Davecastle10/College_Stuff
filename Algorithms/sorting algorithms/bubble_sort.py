# for some reson gitpod doesnt work on library computers
# the code does wor
""" STARTR WITH FIRST ITEM OF THE ARRAY
create coiunter variable
compare it tio the next item
if first item is bigger swap there indexes
repeat whilst iterationg through the array
store index of final item as end variable
reset counter variable to 0
repeat iteration of comparisons
until counter variable = end variable
repeat unil end arible is 1 or 0 (might change on implementaation)
"""
array_test = [1, 2, 99, 87, 1000, 12, 9, 5, 3]# the area being sorted
def bubble_sorting(sorting_array):
    counter = 0# counter var
    end = len(sorting_array)# current endpoint of arr range we are iterating through
    temp = 0# temporary value
    for i in range(len(sorting_array)):# iterates as many times as the array is long
        while counter < end:# while first item index is less than last item in rnage index
            if sorting_array[counter] > sorting_array[counter + 1]:# check value of item with index counter in arr against value of index + 1 in arr
                temp = sorting_array[counter]# asigni arr[counter]'s value to the temp var
                sorting_array[counter] = sorting_array[counter + 1] # switching values over this line and next
                sorting_array[counter + 1] = temp
            if counter > len(sorting_array):# makes sure counter +1 cnat be out of range in other bit of code
                counter += 1# iterating counter by 1
        counter = 0# resetting counter
        end -+ 1# decreasing end by 1
    pass
    return sorting_array# returnin sorted array arr


def array_sort(arr):
    temp = 0
    temp2 = 0
    arr_len = len(arr)
    for i1 in range(arr_len+1):
        for i in range(arr_len-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                temp2 = arr[i+1]
                arr[i] = temp2
                arr[i+1] = temp
    return arr

print(array_sort(array_test))


#print(bubble_sorting(array_test))

