'''
This problem was asked by Apple.
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
For example, given [-6, 0, 2, 40], you should return 2.
Given [1, 5, 7, 8], you should return False.
'''

#_________________________________________________________________

def is_Index(l):
    for i in range(0 ,len(l)):
        if l[i] == i: return True
    else: return False

print(is_Index(eval(input())))
