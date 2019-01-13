"""
 A function to calculate Fibonacci Sequence
 The function adds the previous 2 numbers up to x
"""

import numpy as np

# Simple Recursive Version

def Fib(x):
    """O(2**n) complexity"""
    if x in (0, 1, 2):
        return 1
    return Fib(x-1) + Fib(x-2)



# Dynamic Programming Version
# by using Dictionary(Hash Table) we can store computations
# and recall them from memory(dictionary) if revisiting the same value

memo = {}

def DynamicFib(x):
    """O(1) / O(n) complexity"""
    if x in memo:
        return memo[x]
    if x in (0, 1, 2):
        return 1
    memo[x] = DynamicFib(x-1) + DynamicFib(x-2)
    return memo[x]



# Run locally
if __name__ == '__main__':
    # load previous memo
    try:
        memo = np.load('fib_memory.npy').item()
    except:
        pass

    # User Interface
    while True:
        n = int(input('The nth Fibonacci Number: '))
        try:
            # Dynamic Version
            print('Running dynamic version...\n', DynamicFib(n))
            np.save('fib_memory.npy', memo)
        except RecursionError:
            print("Python Recursion Limit, try something smaller first")
#        else:
#            # Regular Version
#            print('Running regular version...')
#            print(Fib(n))
