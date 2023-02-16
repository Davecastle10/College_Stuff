# Normalised and not normailised numbers

This file has some basic binary arithmetic and some notes about normailsed negative numbers

## Write 9.875 in fixed point binary
9.875 = 1001.111  

## Write -5.375 in 2sC fixed point binary
-8 4 2 1 0.5 0.25 0.125  
1  0 1 0  1   0    1  
-8 + 2 + 0.5 +0.125  
-5.375 = 1010.101  
this is the normalised form as it is themost efficient method of displaying -5.375 in 2sc fixed point binary  
1111010.101 is the same number not normalised  

# Normalised numbers notes
## Normalised 2sC numbers what bits do they start with
1. Positive: 01  
positive normalised 2sC numbers alwasy start with "01"

2. Negative: 10  
negative normailised 2sC numbers usually start with "10"  

Except for in these cases:  
-1 which is 1111 or 1 etc -1 is just 1's  
or 0 which is 0  

## Normalisation is all about not wastinig bits when wriiting out numbers.