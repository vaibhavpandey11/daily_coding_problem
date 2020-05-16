'''
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
'''

#_________________________________________________________

def decodings(n):
    n_decodings = 0
    for i in range(len(n) - 1):
        if 10 <= int(n[i] + n[i+1]) <= 26: n_decodings += 1  # checks whether the combined two digits are ranging between [1, 26]
        
    return n_decodings + 1  # adding 1 to count for single digit-decoding

print(decodings(input()))
