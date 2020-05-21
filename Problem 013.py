'''
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

#________________________________________________________________

string, k, long_substrings = input(), int(input()), (("", 0),)  # 'long_substrings' is the tuple of longest substrings with k distinct characters
substrings = [string[i: i+j] for i in range(len(string)) for j in range(1, len(string) - i + 1)]  # finding all substrings in the input string

for substring in substrings:
    if len(set(substring)) == k and len(substring) > long_substrings[-1][-1]: long_substrings = ((substring, len(substring)),)  # when substring of length greater than that of the previous one is found
    elif len(set(substring)) == k and len(substring) == long_substrings[-1][-1]: long_substrings = long_substrings + ((substring, len(substring)),)  # when substring of length equal to that of the previous one is found

for long_substring in set(long_substrings): print(long_substring[0])  # typecast to set to remove duplicate substrings, if exist
