# a function to check if an array is ordered

def is_ordered(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        else:
            return True

test_arr = [1,2,4,7,2,8,9,12,23,3,5]
print(is_ordered(test_arr))