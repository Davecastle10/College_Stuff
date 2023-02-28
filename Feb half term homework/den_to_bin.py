"""
this program takles a denary number as an input and returns an unsigned binary 
"""

# i broke something when addign the bit to make all outputs 8 bit so im not sure what i brok,
# i need to add the error detecting stuff back in so i can find out where the program breaks

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
        return 00000000
    elif den_num > 255:
        return -1

    power_of_two = 0

    for i in range(den_num):
        if den_num - (2**i) > 0:
            power_of_two = i

    den_num_copy = den_num

    while power_of_two >-2:
        if den_num_copy - 2**power_of_two > 0:
            den_num_copy = den_num_copy - 2**power_of_two

            power_of_two = power_of_two - 1
            bin_list.append(1)

        elif den_num_copy - 2**power_of_two < 0:
            power_of_two = power_of_two - 1
            bin_list.append(0)
            
        elif den_num_copy - 2**power_of_two == 0:
            bin_list.append(1)
            if 2**power_of_two > 0:
                
                while power_of_two - 1 > -1 and loop_counter < 10:
                    power_of_two = power_of_two - 1
                    bin_list.append(0)
                    loop_counter += 1

                bin_num_str = "".join(map(str,bin_list))
                #return bin_num_str

            else:
                bin_num_str = "".join(map(str,bin_list))
                #return bin_num_str

    # add a bit that makes al outputs 8 bit

    if len(bin_list) < 8:
        num_front_padding = 8 - len(bin_list)
        for i in range(num_front_padding):
            bin_list.insert(0, 0)

        bin_num_str = "".join(map(str,bin_list))
        return bin_num_str




print(den_to_bin_function(254))

    

