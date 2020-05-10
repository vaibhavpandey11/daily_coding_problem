'''
This problem was asked by Uber.
Given an array of integers, return a new array such that
each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
#_________________________________________________________________

from functools import reduce

def prod_list(l):
    prod_list = list()
    for i in range(0, len(l)):
        list_excluding_i = l[: i] + l[i+1: ]
        prod_list.append(reduce(lambda x, y: x*y, list_excluding_i))
    return prod_list

print(prod_list(eval(input())))

#_______________________________OR__________________________________

from functools import reduce
import operator
def prod_list(l):
    prod_list = list()
    for i in range(0, len(l)):
        list_excluding_i = l[: i] + l[i+1: ]
        prod_list.append(reduce(operator.mul, list_excluding_i))
    return prod_list

print(prod_list(eval(input())))
