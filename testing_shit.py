foobar = "foobar"
#odds = ""
#for i in range(len(foobar)):
#    if (i+1)%2 > 0:
#        odds = odds + foobar[i]
#print(odds)


print(foobar.upper())
def my_function(x):
  return x[::-1]

mytxt = my_function(foobar)

print(mytxt)
raboof = foobar[::-1]
print(raboof)
my_list = [2,3,4,5]
rever = my_list[::-1]
print(rever)

original_string = "Hello World"
temp = original_string.lower()
new_string = ""
for i in range(len(temp)):
    if temp[i] in "aeiou":
        new_string = new_string + temp[i]
print(new_string)
