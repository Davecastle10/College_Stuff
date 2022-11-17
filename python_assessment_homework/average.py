def find_average(array_of_nums):
    total = 0
    count = 0
    average = 0
    for i in range(len(array_of_nums)):
        total = total + array_of_nums[i]
        count += 1
        average = total / len(array_of_nums)
    return average

print(find_average([1,2,3,4]))
    