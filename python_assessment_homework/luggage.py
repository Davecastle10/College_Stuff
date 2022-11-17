#Write some code that asks a user for their luggage weight and #tells them either 
#"too heavy" if its 25kg or more, "£10 fee" if it's between 10 and 25kg,
# or "No fee" if it's between 0 and 10kg.

lugg_weight = int(input("please enter the weight of your luggage to the closest whole number"))
if lugg_weight < 10:
    print("No fee")
elif lugg_weight < 25:
    print("£10 fee")
else:
    print("Too heavy")
    
