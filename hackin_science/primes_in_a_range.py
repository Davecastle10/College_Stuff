import sympy as sym
print(sym.isprime(3))
txt = ""
my_list = ["helllo bitch", ", ", "fuck you"]
print(my_list)
temp = ""
for i in range(3):
    txt.join(str(my_list[i]))
print(txt)


import sympy as sym# importing the module sympy that is used to check if prime

prime_text = ""# string var to add all primes to
primes_list = []# list to store the primes
for i in range(10000, 10050):# iteration through specified range
    if sym.isprime(i) == True:# checkin if i is a prime
        primes_list.append(i)# if i is prime add to primes_list
primes_list_len = len(primes_list)# length of primes_list
for i in range(primes_list_len):# Iterating thorugh primes list
    temp = str(primes_list[i])# a temp string var to hold the prime with index i
    comma_space = ", "# a string var to stor the comma and space that needs to be added to the prime
    temp3 = temp.join(comma_space)# joining temp and comma_space into one string
    prime_text = prime_text.join(temp3)#joining tmpe 3 to string var prime_text
print(prime_text)# printing string var prime_text

