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
            print(power_of_two)
            print(den_num_copy)
            print(bin_list)
            print('ab')

        elif den_num_copy - 2**power_of_two < 0 and den_num_copy > 0:
            power_of_two = power_of_two - 1
            bin_list.append(0)
            print(power_of_two)
            print(den_num_copy)
            print(bin_list)
            print('bc')
            
        elif den_num_copy - 2**power_of_two == 0:
            bin_list.append(1)
            print(bin_list)
            print("kjgkjg")
            den_num_copy = den_num_copy - 2**power_of_two
            if 2**power_of_two > 0:
                
                while power_of_two - 1 > -1 and loop_counter < 10:
                    power_of_two = power_of_two - 1
                    bin_list.append(0)
                    loop_counter += 1
                    print(power_of_two)
                    print(den_num_copy)
                    print(bin_list)
                    print('cd')

                bin_num_str = "".join(map(str,bin_list))
                return bin_num_str
                print("jjjjj")#
                print(bin_list)

            else:
                bin_num_str = "".join(map(str,bin_list))
                return bin_num_str
                print("jjjjjjjjkkkk")

    # add a bit that makes al outputs 8 bit

    if len(bin_list) <= 8:
        num_front_padding = 8 - len(bin_list)
        for i in range(num_front_padding):
            bin_list.insert(0, 0)
            
            print(power_of_two)
            print(den_num_copy)
            print(bin_list)
            print('de')

        bin_num_str = "".join(map(str,bin_list))
        print(bin_num_str)
        return bin_num_str




#print(den_to_bin_function(100))

"""   
print(bin_list)
print(power_of_two)
print(den_num_copy)
print(ab)
README.md""" 


# this works somwtimes and not others
def den_to_hex(denary_num):



    bin_hex_dict = {
        "0000" : "0",
        "000l" : "1",
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
    print("starting den to hex conversion")
    if len(binary_num_str) % 4 != 0:# thsi makes its so the binary number is a multiple of 4 long
        for i in range(len(binary_num_str) % 4):
            print(len(binary_num_str) % 4)
            print(binary_num_str)
            binary_num_str = "0" + binary_num_str
            print(binary_num_str)

    
    print(len(binary_num_str)//4)
    print(binary_num_str)

    hex_num_list = []

    for i in range(len(binary_num_str)//4):# finds the incusive start and exclusive end positions fro the string splicing for comparing hex and binary nibbles
        if i == 0:
            start_pos = 0
            end_pos = 4

        else:
            start_pos = i * 4 # this will be used inclusively
            end_pos = start_pos + 4 # this will be used exclusively

        #for i in range(len(binary_num_str)//4):
        hex_num_list.append( bin_hex_dict.get(binary_num_str[start_pos:end_pos]))
        


        
    hex_num_str = "".join(map(str,hex_num_list))
    print('returning hex num now')
    return hex_num_str

print (den_to_hex(201))
        



