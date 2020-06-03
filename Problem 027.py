'''
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])", you should return true.
Given the string "([)]" or "((()", you should return false.
'''

#________________________________________________________________

def findMaxLen(string):
    stack, valid_length = [], 0 
    stack.append(-1) 
    
    for i in range(len(string)):
        if string[i] in ('(', '[', '{'): stack.append(i)
        else:
            stack.pop()            
            if len(stack): valid_length = max(valid_length, i - stack[-1])
            else: stack.append(i)
    return valid_length

scopes = input()
if findMaxLen(scopes) == len(scopes): print(True)
else: print(False)
