'''
This problem was asked by Twitter.
Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

#________________________________________________________________

def autocomplete(l, x):
    pre_names = []
    for i in l:
        if i.startswith(x): pre_names.append(i)
    return '[' + ', '.join(pre_names) + ']'  # since the names in the result aren't enclosed within inverted commas

names = [name.strip() for name in input()[1: -1].split(',')]  # necessary to take input in such a way, since the names aren't enclosed within inverted commas 
prefix = input()

print(autocomplete(names, prefix))
