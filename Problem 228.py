'''
This problem was asked by Twitter.
Given a list of numbers, create an algorithm that
arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
'''

#_________________________________________________________

list_n = eval(input())
list_n = list(map(str, list_n))
for i in range(0, len(list_n)):
    for j in range(0, len(list_n)-1):
        if len(list_n[j]) == len(list_n[j + 1]):  # if two numbers have equal number of digits
            list_n[j], list_n[j+1] = str(max(int(list_n[j]), int(list_n[j+1]))), str(min(int(list_n[j]), int(list_n[j+1])))
        elif len(list_n[j]) > len(list_n[j + 1]):  # if first number has greater number of digits than the second one
            for k in range(0, len(list_n[j + 1])):
                if int(list_n[j][k]) <= int(list_n[j + 1][k]):
                    list_n[j], list_n[j + 1] = list_n[j + 1], list_n[j]
                    break
        elif len(list_n[j]) < len(list_n[j + 1]):  # if first number has lesser number of digits than the second one
            for k in range(0, len(list_n[j])):
                if int(list_n[j][k]) < int(list_n[j + 1][k]):
                    list_n[j], list_n[j + 1] = list_n[j + 1], list_n[j]
                    break
print(''.join(list_n))

#_____________________OR________________________________

from itertools import permutations
def maximize(list_n):
    n, l = 0, permutations(list_n)
    for i in l:
        temp = ""
        for j in i: temp += str(j)
        n = max(n, int(temp))
    return n
print(maximize(eval(input())))
