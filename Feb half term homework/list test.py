def listToString(s):
   
    # initialize an empty string
    str1 = " "
   
    # return string 
    return (str1.join(s))
       
       
# Driver code   
s = ['Geeks', 'for', 'Geeks']
print(listToString(s))

bin_list = [1,0,1,0]
print("".join(map(str,bin_list)))