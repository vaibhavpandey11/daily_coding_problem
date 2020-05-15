'''
Given a list of numbers, return whether any two sums to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
#__________________________________________________________

from itertools import combinations

def check(nums, s):
    for com in combinations(nums, 2):
        if sum(com) == s: return True
    else: return False

l = list(map(int, input().split(' ')))
s_input = int(input())
print(check(l, s_input))
