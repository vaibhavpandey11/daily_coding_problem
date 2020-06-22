'''
This problem was asked by Google.
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
For example, the edit distance between "kitten" and "sitting" is three: substitute the "k" for "s", substitute the "e" for "i", and append a "g".
Given two strings, compute the edit distance between them.
'''

#________________________________________________________________

def edit_dist(string1, string2):
    edit_distance = 0

    edit_distance += abs(len(string2) - len(string1))
    for i in range(min(len(string1), len(string2))):
        if string1[i] != string2[i]: edit_distance += 1

    return edit_distance

print(edit_dist(input(), input()))
