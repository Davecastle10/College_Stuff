"""
this program takles a denary number as an input and returns an unsigned binary 
"""

""" plan:

    take inpuit as a var
    see what the largest power of two that can be subtracted whilst keppin num positive is
    stor that power of two as a var called biggest power of 2 as example
    keep checking power of twos and if yess add a 1 to a list and if no add a 0 to the list and check the next smallest power of 2 by subtracting 1 fromn the power of two var
    continue this until the denary  number rem,aing after subtraction is 0
    if inputeed number is greater than 255 returns -1
"""

def den_to_bin_function(den_num):
    loop_counter = 0

    bin_list = []

    if den_num == 0:
        return 0
    elif den_num > 255:
        return -1

    power_of_two = 0

    for i in range(den_num):
        if den_num - (2**i) > 0:
            power_of_two = i

    #print(power_of_two)   #this was for testing

    den_num_copy = den_num

    while power_of_two >-2:
        if den_num_copy - 2**power_of_two > 0:
            den_num_copy = den_num_copy - 2**power_of_two
            print(power_of_two)
            power_of_two = power_of_two - 1
            bin_list.append(1)
            print('o7t0yf')
            print(bin_list)
            print(den_num_copy)
            print(power_of_two)

        elif den_num_copy - 2**power_of_two < 0:
            power_of_two = power_of_two - 1
            bin_list.append(0)
            print(power_of_two)
            print('kjgkjgkjg')
            print(den_num_copy - 2**power_of_two)
            


        elif den_num_copy - 2**power_of_two == 0:
            print("dfgsfg")
            print(bin_list)
            bin_list.append(1)
            if 2**power_of_two > 0:
                print(power_of_two - 1) 
                while power_of_two - 1 > -1 and loop_counter < 10:
                    power_of_two = power_of_two - 1
                    print(power_of_two)# bug testing
                    bin_list.append(0)
                    print("oooo")# bug testing
                    loop_counter += 1

                bin_num_str = "".join(map(str,bin_list))
                print("elif if path")
                print(bin_list)
                return bin_num_str

            else:
                print("elif else path")
                bin_num_str = "".join(map(str,bin_list))
                return bin_num_str
        else :
            print(den_num_copy - 2**power_of_two)
            print("else")




print(den_to_bin_function(255))

    

