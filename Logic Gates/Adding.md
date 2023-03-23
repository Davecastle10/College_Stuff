# Adding with logic gates

## Half Adder
On the **ALU** (Arithmetic and Logic Unit)
to add 2 bits we need a circuit with a **Carry** and  **Sum**  

| A | B | Carry | Sum |  
| ----------- | ----------- | ----------- | ----------- |
| 0  | 0 | 0 |  0 |
| 0  | 1 | 0 |  1 |  
| 1  | 0 | 0 |  1 |
| 1  | 1 | 1 |  0 |


| A | B | Carry (AND) |  
| ----------- | ----------- | ----------- |
| 0  | 0 | 0 |
| 0  | 1 | 0 |  
| 1  | 0 | 0 |
| 1  | 1 | 1 |

| A | B | Sum (XOR)|  
| ----------- | ----------- | ----------- |
| 0  | 0 | 0 |
| 0  | 1 | 1 | 
| 1  | 0 | 1 |
| 1  | 1 | 0 |