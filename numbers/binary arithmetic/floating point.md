# Floating point numbers
## Basic eplanantion of terms
We have a Mantissa and an Exponent   
Mantissa is the significant digits  
Exponent is times 2 to the power ______  
### The Mantissa andthe Exponent are both in 2sC
## Example
### For an 8 bit Mantissa and a 6 bit exponent:
Convert the following 2sC float into denary:  

mantissa exponent  
01101010 001111  
0.1101010 001111  
shift the decimal point 15 places to the left  
= 011010100000000.  
= 27,136 (in denary)  

## Rules
1. The decimal point is after the most significant bit, just like standard form
2. for positive pad to the left wiht 0's wheeas dfor negative pad to the left with 1's

## Pracice questions
1. 01100000 000011  
= 0.1100000 d.p 3 to the right  
= 0110.0000
= 6 (denary)

2. 01001110 000101  
= 0.1001110 d.p 5 to the right  
= 010011.10  
= 19.5 (denary)

3. 01100000 111111  
= 0.1100000 d.p -1 to the right / 1 to the left  
= 0.01100000   
= 0.375 (denary)

4. 10100000 000001
= 1.0100000 d.p 1 to the right  
= 10.100000  (-2 + 0.5 = -1.5)
= -1.5 (denary)  

5. 10100000 111100
= 1.0100000 d.p -4 to the right / 4 to the left
= 1.11110100000
= -0.046875 (denary)  
or  
= _.___(-1)01000  
= _.___(-1) = -1/16  
= _.___001 = 1/64  
= (-1/16)+1/64  
= -0.046875