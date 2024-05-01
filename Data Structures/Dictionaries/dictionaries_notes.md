# Dictionaries

## Basic explanation 

Dictionaries are a data structure based on hash maps. Each entry in a dictionary is composed of a (key, value) pair with the value being the data stored in that entry and the key being the the data that is hashed to retrieve the value from the dictionary. E.g. If you have 10 buckets of space in the dictionary the key could be 99,and you could put 99 into the hashing function x MOD 10 which would give the result of the value going into bucket 9 in the dictionary.  

They have a data retrieval if O(1). 