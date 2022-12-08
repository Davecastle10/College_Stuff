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
        return check_index
    elif check_index == len(items):
        return -1
    else:
        #base case
        print(check_index)
        linear_search_recursive(items, check_index + 1, search_item)
    



#try to complete a recursive binary search, returning the index of the item, or -1
def binary_search_recursive(items, search_item):
    #base cases
    #recursive case:

    pass

"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
that divides evenly into both of them. For example, the gcd(102, 68) = 34.
We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

#tests
#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#
#print (factorial(4))
#countdown(10)
#print(fibonacci(10))
print(linear_search_recursive([1,2,3,4,5,6], 0, 5))