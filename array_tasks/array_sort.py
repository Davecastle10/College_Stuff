test_arr = [1,2,4,7,2,8,9,12,23,3,5]

# function to sort an array 
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

print(array_sort(test_arr))