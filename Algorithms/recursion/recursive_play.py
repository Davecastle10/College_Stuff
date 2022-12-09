import time

#Converts a positive number to a binary represented as a list of 0s and 1s.
#using the algorithm of divide by 2 and put the remainder in the small column then start again with the quotient as input
def pos_dec_to_binary(decimal,bit_list):
    if decimal<=1:
        bit_list.append(decimal%2)
        return list(reversed(bit_list))
    else:
        bit_list.append(decimal%2)
        return pos_dec_to_binary(decimal//2,bit_list)
    
#why does this not work? Fix it!
def countdown(number):
    if number > -1:# base case
        print(number)
        time.sleep(1)
        countdown(number-1)# recursive case


#try to complete this
def fibonacci(n):# works now
    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + fibonacci(n-1)
    #recursive case: the fibonacci number is the sum of the previous 2

#triangular numbers
def triangular(n):
    if n == 1:
        return 1# base case
    else:
        return n + triangular(n-1)# recursive case

#try to complete this
def factorial(input_number):
    #5 fact = 5 x 4 x 3 x 2 x 1
    if input_number == 1:# base case
        return 1
    else:
        return input_number * factorial(input_number-1)# recursive case



#try to complete a recursive linear search, returning the index of the item, or -1
""" doesn't work for some reason"""
def linear_search_recursive(items, check_index, search_item):
    #base cases
    if items[check_index] == search_item:
        print(" if stat")
        print(items[check_index])
        print(check_index)
        return check_index# retur index of the search_item
        #this works but doesnt return on previous line

    elif check_index == len(items):
        print("elif stat")
        return -1# search_item is not there

    else:
        print(check_index)
        return linear_search_recursive(items, check_index + 1, search_item)# recursive case
    



#try to complete a recursive binary search, returning the index of the item, or -1
def binary_search(entered_list, item, index, low, high):
    """ list must be orderd
    go to middle of list
    compare value to item
    if bigger ignore bigger half of list and vice bversa
    repeat until item is found or if item is not present
    output either index or true if item is present based on the value of index parameter
    or false if item is not present"""
    # not all comments will be correct, nut the ones in the recurswive binary search file in searching algorithms folder should be
    middle_index = (low + high)//2# finds the index of the middle value in the list
    if entered_list[middle_index] == item:# is middle val of list item
        if index == True:# is index true
            print(middle_index)# if yes return and print index of middle value, which would be the earliest index of the item
            return middle_index
        elif index == False:
            print(True)# return and print True if item is in list
            return True
    elif entered_list[high] < item or entered_list[low] > item:#if search item is greater than largest value in list it is not there
        if index == True:# is index true
            return -1
        elif index == False:
            return False
    elif entered_list[middle_index + 1] == item:# copy of code above with variations so it checks the next value to so that if item is lats in list it doenst casue infinte loop
        if index == True:# is index true
            return middle_index + 1
        elif index == False:
            return True    
    elif low == high:# else return false  - if you get rid of this elif stuff it loops infintely
        if index == True:# is index true
            return -1
        elif index == False:
            return False
    elif item < middle_index + 1:# if item is less than middle value
               return binary_search(entered_list, item, index, low, middle_index)# call function with botto  half of list instead of total list
    elif item > middle_index - 1:# if item is greater than middle value
                return binary_search(entered_list, item, index, middle_index, high)# call funcio again with top half of list
    
  

"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
that divides evenly into both of them. For example, the gcd(102, 68) = 34.
We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q."""


test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]# witho
#tests
#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#
#print (factorial(4))
#countdown(10)
#print(fibonacci(10))
#print(f"this is uindex {linear_search_recursive(test_list, 0, 5)}")


print(f"index of search item is {binary_search(test_list, 9, True, 0, len(test_list)-1)}")