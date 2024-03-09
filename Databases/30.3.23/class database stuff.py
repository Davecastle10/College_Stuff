our_class = [[0,"George","regular show", "Balthazar"],
         [1,"Matt","Spongebob", "Tim"],
         [2,"Dmitrii","Nickolodeon", "Tom"],
         [3,"Oliver","Cartoon Network", "Frodo"],
         [4,"Trokhym","QTV", "Max"],
         [5,"Zack","Better call Saul", "Francesca"],
         [6,"Jack","Breaking Bad", "Oscar"],
         [7,"Chris","Slimesickle", "N/A"],
         [8,"David","Mythbusters", "Sid"],
         [9,"Abin","Spots18", "Snakey"]]

""" Print all the rows in the 2d array"""
def output_all_rows():
    for i in range(len(our_class)):
        print(our_class[i])

#output_all_rows()

"""A function that returns true if the name passed in is one of the members of the class"""

# could also add a parmater to pass the 2d array into the function -done
def class_name(name, two_dimensional_array):
    for i in range(len(two_dimensional_array)):
        if name in two_dimensional_array[i][1]:
            return True
    return False

#print(class_name("David", our_class))

""" A function that sorts the items by order of name"""
#declaritive, but try an imperative one
def decl_table_sort(field):
    sorted_list = sorted(our_class, key = lambda x: x[field] )
    return sorted_list

#print(decl_table_sort(1))

def imp_table_sort(field):
    arr = []
    for i in range(len(our_class)):
        arr.append(our_class[i][field])

    temp = 0
    temp2 = 0
    arr_len = len(arr)
    for i1 in range(arr_len+1):
        for i in range(arr_len-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                temp2 = arr[i+1]# this line and one below are not needed, could just have arr[i] = arr[i+1]
                arr[i] = temp2
                arr[i+1] = temp

    for i in range(len(arr)):
        string_temp = arr[i]
        for g in range(len(our_class)):
            if string_temp in our_class[g][field]:
                arr[i] = our_class[g]

    return arr


print(imp_table_sort(1))


# testing if str can be compared greater/less than
if "add" < "bok":
    print("kjdff")
