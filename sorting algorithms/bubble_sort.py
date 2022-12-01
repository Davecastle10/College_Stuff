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
array_test = [1, 2, 99, 87, 12, 9, 5, 3]# the area being sorted
def bubble_sorting(arr):
    counter = 0# counter var
    end = len(arr)# current endpoint of arr range we are iterating through
    temp = 0# temporary value
    for i in range(len(arr)):# iterates as many times as the array is long
        while counter < end:# while first item index is less than last item in rnage index
            if arr[counter] > arr[counter + 1]:# check value of item with index counter in arr against value of index + 1 in arr
                temp = arr[counter]# asigni arr[counter]'s value to the temp var
                arr[counter] = arr[counter + 1] # switching values over this line and next
                arr[counter + 1] = temp
            counter += 1# iterating counter by 1
        counter = 0# resetting counter
        end -+ 1# decreasing end by 1
    return arr# returnin sorted array arr



print(bubble_sorting(array_test))