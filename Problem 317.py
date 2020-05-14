'''
This problem was asked by Yahoo.
Write a function that returns the bitwise AND of all integers between M and N, inclusive.
'''

#___________________________________________________________________

def bitwise_AND(M, N):
    if len(M): return [M[0] & N[0]] + bitwise_AND(M[1: ], N[1: ])
    else: return []

print(bitwise_AND(eval(input()), eval(input())))
