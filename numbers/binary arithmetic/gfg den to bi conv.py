#decimal to bionary cpnverter from geeks for geeks but it is on a lot of other websites.

def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 128
     
    # Calling function
    DecimalToBinary(dec_val)