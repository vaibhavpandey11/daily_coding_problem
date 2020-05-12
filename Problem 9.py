'''
This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''

#_________________________________________________________

def largest_sum(l):
    l_sum = 0
    for i in range(0, len(l) - 2):
        for j in l[i+2: ]: l_sum = max(l_sum, l[i] + j)
    return l_sum

print(largest_sum(eval(input())))
