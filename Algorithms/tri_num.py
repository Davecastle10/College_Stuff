def trinum(n):
    if n == 1:
        return 1# base case
    else:
        return n + trinum(n-1)# recursive case


print(trinum(12))

def fact_num(n):
    #5 fact = 5 x 4 x 3 x 2 x 1
    if n == 1:# base case
        return 1
    else:
        return n * fact_num(n-1)# recursive case


print(fact_num(900))