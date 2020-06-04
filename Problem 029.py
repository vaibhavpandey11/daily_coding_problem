'''
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

#________________________________________________________________

def encode(string):
    encoded_str, letter_and_count = "", [1, string[0]]
    for i in range(1, len(string)):
        if string[i] == letter_and_count[1]: letter_and_count[0] += 1
        else:
            encoded_str += str(letter_and_count[0]) + letter_and_count[1]
            letter_and_count = [1, string[i]]
    else:  encoded_str += str(letter_and_count[0]) + letter_and_count[1]  # encoding the last letter of string, which is missed in the last iteration
    return encoded_str

def decode(string):
    decoded_str = ""
    for i in range(0, len(string), 2): decoded_str += string[i+1] * (int(string[i]))
    return decoded_str

# print(encode("AAAABBBCCDAA"))
# Output: 4A3B2C1D2A
# print(decode("4A3B2C1D2A"))
# Output: AAAABBBCCDAA

# print(encode("HHEEELOOOO"))
# Output: 2H3E1L4O
# print(decode("2H3E1L4O"))
# Output: HHEEELOOOO
