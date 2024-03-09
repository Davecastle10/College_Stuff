"""
this file contains two functions, one that converts denary numbers between 255 and 0 inclusive into 8 bit unsigned binary numbers,
and another that uses the first to convert denary numbers (with the same size limitations) into 2 digit hexadecimal numbers 
"""
# ive purposefully made these functions less efficient tha they could be so i would have to use more problem solving and have more fun whilst making them.

def den_to_bin_function(den_num):
    loop_counter = 0# a counter to prevent infinite loops later on in the larger while loop section

    bin_list = []# the list that the binary digits are inserted in

    if den_num > 255 or den_num < 0: # sees if den num is out of bounds of an unsigned 8 bit binary number
        return -1

    power_of_two = 0 # var to strore the order of the power of 2 that the current digit is

    for i in range(den_num):# works out the maximum order of 2 is required for the binary number e.g order 7 is 2**7 = 128
        if den_num - (2**i) > 0:
            power_of_two = i


    while den_num > 0:# the main loop that actually gets stuff done
        if den_num - 2**power_of_two > 0:# if den_num - 2**power_of_two is positive add 1 to the binary number
            den_num = den_num - 2**power_of_two
            power_of_two = power_of_two - 1# decrease the value of power_of_two by 1 so that next binary place can be checked to see if it neeeds to be a 1 or 0
            bin_list.append(1)
            # the green comments in the main code are for bug fixing

        elif den_num - 2**power_of_two < 0 and den_num > 0:# if den_num - 2**power_of_two is negativ add o to the binary number 
            power_of_two = power_of_two - 1# decrease the pwer f two so that the next figot of the bianry number is checked
            bin_list.append(0)

        elif den_num - 2**power_of_two == 0:# this is so that numbers like 128 are represented properly as 1000 0000 and not 1 and have all the correct trailling 0's
            bin_list.append(1)

            den_num = den_num - 2**power_of_two# decrease the power of 2 to check neck binary digit
            if 2**power_of_two > 0:# if there are still orders of 2 go through
                
                while power_of_two - 1 > -1 and loop_counter < 10:# adds as many trailing 0 are needed so the binary num is corrct
                    power_of_two = power_of_two - 1
                    bin_list.append(0)
                    loop_counter += 1# makes sure the program doesnt accidently run in infinte loops, it did that a lot before adding this

    # makes all outputs 8 bit
    #print("dfdfdfdfdfdf")
    if len(bin_list) <= 8:
        num_front_padding = 8 - len(bin_list)
        for i in range(num_front_padding):
            bin_list.insert(0, 0)

        # makes the binary list into a string
        bin_num_str = "".join(map(str,bin_list))
        # returns the binary number string 
        return bin_num_str




#print(den_to_bin_function(169))



# this converts denary to hex by using the previous function to convert den to bin and then converts the bin to hex

def den_to_hex(denary_num):
    # this is a dictionary conating all 4 bit binary values and their corresponding hex values
    bin_hex_dict = {
        "0000" : "0",
        "0001" : "1",
        "0010" : "2",
        "0011" : "3",
        "0100" : "4",
        "0101" : "5",
        "0110" : "6",
        "0111" : "7",
        "1000" : "8",
        "1001" : "9",
        "1010" : "A",
        "1011" : "B",
        "1100" : "C",
        "1101" : "D",
        "1110" : "E",
        "1111" : "F",
    }

    binary_num_str = den_to_bin_function(denary_num)

    hex_num_list = []# list containg hex digits

    for i in range(len(binary_num_str)//4):# finds the incusive start and exclusive end positions fro the string splicing for comparing hex and binary nibbles
        if i == 0:
            start_pos = 0
            end_pos = 4

        else:
            start_pos = i * 4 # this will be used inclusively
            end_pos = start_pos + 4 # this will be used exclusively

        #for i in range(len(binary_num_str)//4):

        print(bin_hex_dict.get(binary_num_str[start_pos:end_pos]))
        hex_num_list.append( bin_hex_dict[binary_num_str[start_pos:end_pos]])
        
    hex_num_str = "".join(map(str,hex_num_list))
    return hex_num_str

print(den_to_hex(15))
        



