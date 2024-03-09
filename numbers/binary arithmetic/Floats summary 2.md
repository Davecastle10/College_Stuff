# Floats
**Mantissa** (significant bits)   **Exponent** (*2^what number? - shift)  
## **E.g.** represent -17.5 in normalised 2sC float representation, using as few bits as possible for the mantissa and exponent  
-32 16 8 4 2 1 0.5 
1   0  1 1 1 0. 1  need to move d.p (technically b.p) 5 places to left  
1.011101 so now exponent
1011101 0101

## Then do 31.0625 in the same format
-32 16 8 4 2 1 .5 .25 .125 .0625  
0    1 1 1 1 1 0   0   0    1  
011111.0001 need to move b.p 5 to the left  
0.111110001   0101  
31.0625 = 0111110001   0101  

## Add theses floats
**Mantissa is 5 bits and exponent is 3 bits 2sC numbers** 
you need to line up the decimal points and the you can do the arithmetic as usual

01101 010 = 011.01  
01110 001 = 01.110  


0001.110  
0011.01   
- - - - 
0101.000  
convert to float  
0.1010 d.p needs to move 3 to right  
01010 011

