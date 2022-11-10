#create an array of 20 ints
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#print them all
print(my_array)
#print the 5th item
print(my_array[4])
#print the fith to the 9th items
print(my_array[4:9])
#print the array in reverse
print(my_array[::-1])



# function to sort an array 
def array_sort(arr):
    temp = 0
    temp2 = 0
    arr_len = len(arr)
    for i in range(arr_len-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            temp2 = arr[i+1]
            arr[i] = temp2
            arr[i+1] = temp
    return arr







print(array_sort([1,10,3,2,5,8,6,4,9]))