def search(sorted_list, item):	

    for i in range(len(sorted_list)):
        if sorted_list[i] == item:
            return True
    return False

print(search([1,2,3,4,5], 3))