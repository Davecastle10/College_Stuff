import random
test_arr = [1,2,4,7,2,8,9,12,23,3,5]

# array shuffler
def array_shuffle(arr):
    temp_arr = []
    arr_index_list = []
    temp_arr_index_list = []
    item = 0
    arr_index = 0
    arr_len = len(arr)
    for i in range(arr_len):
        temp_arr.append(0)
    for i in range(arr_len):
        arr_index_list.append(i)
    for i in range(arr_len):
        temp_arr_index_list.append(i)
    for i in range(arr_len):
        arr_index = random.choice(arr_index_list)
        temp_arr_index = random.choice(temp_arr_index_list)
        arr_index_list.remove(arr_index)
        temp_arr_index_list.remove(temp_arr_index)
        temp_arr[temp_arr_index] = arr[arr_index]
    return(temp_arr)

#print(test_arr)
#print(array_shuffle(test_arr))