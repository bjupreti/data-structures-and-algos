"""
Write a fuction fib(n) that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.
"""
def fib(n, memo = {}):
    """
    Takes in a number as an argument and return the n-number of the Fibonacci sequence.
    """
    if n in memo:
        return memo[n]
    else:
        if n <= 2:
            return 1
        memo[n] = fib(n - 1, memo) + fib(n -2, memo)
        return memo[n]
    
    
print(fib(2))
print(fib(50))