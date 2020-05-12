'''
This problem was asked by Quora.
You are given a list of (website, user) pairs that represent users visiting websites.
Come up with a program that identifies the top k pairs of websites with the greatest similarity.
For example, suppose k = 1, and the list of tuples is:
[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].
'''

#______________________________________________________________________________

# letters -> websites | numbers -> user_identity
# We assume that the input is in the following format -
# [('a',1),('a',3),('a',5),('b',2),('b',6),('c',1),('c',2),('c',3),('c',4),('c',5),('d',4),('d',5),('d',6),('d',7),('e',1),('e',3),('e',5),('e',6)]

l = eval(input())
sites_users, k = [[l[0][0], []]], l[0][0]  # initialising list with list_pairs of website and users in format: [website, [users]]; k stores website for creating new key purpose

for i in range(0, len(l)):
    if l[i][0] == k: sites_users[len(sites_users) - 1][1].append(l[i][1])  # when website doesn't changes, updates the set of values by type casting it into list so as to append easily
    else:
        k = l[i][0]  # changes the value of k key; 
        sites_users.append([l[i][0], [l[i][1]]])  # appends new list_pair of website and users in format: [website, [users]]

similarity_list = list()  # contains data in format: (first website, second website, number of common users of both the sites, number of uncommon users of both the sites)
for i in range(0, len(sites_users)-1):
    for j in range(i+1, len(sites_users)):
        similarity = len(set(sites_users[i][1]).intersection(sites_users[j][1]))  # number of common users of both the sites
        difference = abs(max(len(sites_users[i][1]), len(sites_users[j][1]))- similarity)  # number of uncommon users of both the sites
        similarity_list.append((sites_users[i][0], sites_users[j][0], similarity, difference))

similarity_list.sort(key = lambda x: x[2], reverse = True)  # sorting in descending order(max to min), according to similarity
for i in range(0, len(similarity_list)):
    for j in range(0, len(similarity_list) - 1):  # sorting in ascending order, according to difference, but maintaining the similarity
        if similarity_list[j][2] == similarity_list[j+1][2] and similarity_list[j][3] > similarity_list[j+1][3]: similarity_list[j], similarity_list[j+1] = similarity_list[j+1], similarity_list[j]

print([(similarity_list[i][0], similarity_list[i][1]) for i in range(int(input()))])  # top n pairs in similarity_list
