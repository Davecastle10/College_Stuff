""" This is an example of a dictionary that stores the test results of some students
"""

results = {"Detra": 17,
       "Nova": 70,
       "Dave": 71,
       "John": 63,
       "Chris": 29,
       "Elon": 28}

# the green text on the left of each : is the key for the pair
# and the pink text on the left of each pair is the value

""" basic retrieval"""

print(results["Dave"])
# prints the value associated with the key "Dave" in the dictionary results



""" This is an example of retriving data from a dictionary and using it to work out the class average score as an integer
"""

#results_key_list = list(results.keys())[1]
average = 0
total = 0
for i in range(len(results)):
    total = total + results[list(results.keys())[i]]
average = int(total/len(results))
print(average)

""" adding a new entry to a dictionary is simple"""

# just type the dictionary name and enter a new key that is not currrently in use,
# into the square brackets, and set the line = to the valu you want to pair with the new key

results["Jake"] = 20

print(results["Jake"])
# this line creates a new entry in the dictionary with Key = "Jake" and Value = 2000#

""" Updating a value in a dictionary"""


print("Daves scrore before remarking", results["Dave"])
results["Dave"] = 100
print("Daves Score after remarking", results["Dave"])


""" Removing a value stored in the dictionary """

results.pop("Elon")

