'''
This problem was asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

#________________________________________________________________

# This is solution to the first part of the problem, where the steps at a time may be 1 or 2.
from itertools import permutations
def unique_ways(n):
    ways, max_iter, steps = 0, n//2 + 1, tuple(1 for i in range(n))

    for i in range(max_iter):
        ways += len(set(permutations(steps)))
        try:  # used to avoid exception at the last iteration which is necessary, as it adds 1 to the no. of 'ways', but does not find 1 in 'steps'
            one_index = steps.index(1)  # index() raises ValueError exception if index not found; hence, try-except is necessary
            if steps[one_index + 1] == 1: steps = steps[: one_index] + (2,) + steps[one_index + 2: ]  # converts [1, 1] into [2]
        except: pass  # suppresses ValueError
    return ways
    
print(unique_ways(int(input())))
