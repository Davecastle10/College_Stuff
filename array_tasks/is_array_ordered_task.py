# a function to check if an array is ordered
# this doesn't work
def is_ordered(arr):
    for i in range(len(arr)):
        if arr[i+1] < arr[i]:
            return False
        
    return True# moved this line to be in line with the start of the for loop instead of under an else: statement by the if: statement to see if it runs hopefully. 

test_arr = [1,2,4,7,2,8,9,12,23,3,5]
print(is_ordered(test_arr))


