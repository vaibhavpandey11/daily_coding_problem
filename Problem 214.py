'''
This problem was asked by Stripe.
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
For example, given 156, you should return 3.
'''

#___________________________________________________________________

n = int(input())
bin_n = bin(n)[2:]  # binary format of input number
# appends all collections of '1' in a list
one_list = [i for i in bin_n.split("0") if i != '']
one_list.sort(key=len)  # sorts the list on the basis of length of collections of '1's
print(len(one_list[-1]))
