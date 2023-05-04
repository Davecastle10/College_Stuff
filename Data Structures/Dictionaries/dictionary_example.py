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


""" This is an example of retriving data from a dictionary and using it to work out the class average score as an integer
"""

#results_key_list = list(results.keys())[1]
average = 0
total = 0
for i in range(len(results)):
    total = total + results[list(results.keys())[i]]
average = int(total/len(results))
print(average)