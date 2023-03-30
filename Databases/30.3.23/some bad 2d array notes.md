# dave drew a 2d pyton array on the whiteboard
## array?

| ID | Name | FavoriteTV | Pet |  
| ----------- | ----------- | ----------- | ----------- |
| 0  | George | Regular Show |  Balthaazar |
| 1  | Matt | Spongebob |  Tim |  
| 2  | Dmitrii | Nickolodeon |  Tom |
| 3  | Oliver | Cartoon Network |  Frodo |
| 4  | Trokhym | QTV |  Max |
| 5  | Zack | Better call Saul |  Francesca |  
| 6  | Jack | Breaking Bad |  Oscar |
| 7  | Chris | Slimesickle |  N/A |
| 8  | David | Mythbusters |  Sid |
| 8  | Abin | Spots18 |  Snakey |


## Questions 
1. `print(4,3)`  
    outputs nothing as didnt call data structure  

2. `print(class[4][3]`   
    outputs "Max" which is the name of Trokhyms pet

3. `class[0][2] = "MOTD"`  
    `print(class[0])`  
    changes georges favorite show from "Regular Show" to "MOTD"  
    outputs *0, George, Regular Show, Balthazar*

4. `print(len(class))`  
    outputs 10 as python treats the 2d array as an array with 10 nested arrays in it

5. `print(len(class[3]))`  
    outputs the length of the (0,1,2,3) 4th row which is 4 as all the rows have 4 full fields
