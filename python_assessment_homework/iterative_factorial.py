def iterative_factorial(n):
    """A function that returns the factorial or n. The factorial of n 
where n is 3 is calculated by 3 * 2 * 1, so is 6 """
    x = n
    fact = 1
    for i in range(n):
        fact = fact * x
        x = x - 1
    return fact

print(iterative_factorial(7))

