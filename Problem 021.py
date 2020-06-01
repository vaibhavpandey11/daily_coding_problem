'''
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

#________________________________________________________________

# taking input and sorting the periods in ascending order according to starting time of lecture
intervals = sorted(eval(input()), key = lambda x: x[0])

class_l = list()  # list of classrooms, where each classroom contains a list of lectures
class_l.append([intervals[0]])  # appending a list containing first lecture

for i in range(1, len(intervals)):
    for j in range(0, len(class_l)):
        if intervals[i][0] > class_l[j][-1][1]:
            class_l[j].append(intervals[i])
            break
    else: class_l.append([intervals[i]])

print(len(class_l))  # no. of classrooms

# to print classrooms containing list of lectures in each classroom -
# for i in class_l: print(i)
            
