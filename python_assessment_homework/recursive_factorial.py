def recursive_factorial(n):
    """A recursive function that returns the factorial or n. The factorial of n 
where n is 3 is calculated by 3 * 2 * 1, so is 6 """

    if n == 0:
        return o
    elif n == 1:
        return 1
    else:
        return (n * recursive_factorial(n-1))
