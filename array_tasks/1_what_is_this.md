# Array Tasks
this is a folder with work done playing around with arrays and lists in python

Arrays are a list that is composed of only one data type and you must declare its length upon its creation. 
Arrays are more effuicint to search through for entrys than lists.
Arrays must be contiguously indexed, meaning that the list is in one large data block in RAM with nothing seprrating the array into sections.



## 5 facts about arrays:

1. Arrays are contiguous, meaning that the array is in one large block of data in RAM, not several smaller blocks, so each entry in the array has the next address in RAM after the previous entry.
2. Arrays have a predefined length that is declared upon their creation.
3. Items in an array all have the same data type, (they are homogenous in their data types).
4. In python you creat an array by going my_array = [] (arrays in python dont have to have a predefined length).
5. Arrays are a data structure that allow for convenient and quick accesing/storaging of data in an organised/structured way.
6. All items in an array are the same size.
7. If each item in an array is 5 bytes and you want the 1001'th item, then you go to the (1000*5) = 5000th byte which contains the first byte of the data you want.