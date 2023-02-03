# Binary arithmetic
## These is some examples of binary arithmetic
SaM ->   -  64 32 16 8 4 2 1
2sc -> -128 64 32 16 8 4 2 1

## represent these as bytes
### 54
SaM - 00110110  
2sC - 00110110

### -54
SaM - 10110110  
2sC - 11001010
### 0 in three ways  
SaM - 00000000 = 0  
SaM - 10000000 = -0  
2sc - 00000000 = 0  

### 12.875 in fixed point notation
grid 128 64 32 16 8 4 2 1 . 1/2 1/4 1/8 
      0  0  0  0  1 1 0 0 .  1   1   1  
12.875 = 00001100.111

### -34.5 
(done in SaM)  
grid  - 64 32 16 8 4 2 1 . 1/2 1/4 1/8  
      1  0  1  0 0 0 1 0 .  1   0   0  
-34.5 = 10100010.100  
  
(done in 2sC)
grid  -128 64 32 16 8 4 2 1 . 1/2 1/4 1/8  
        1   1  0  1 1 1 0 1 .  1   0   0  

