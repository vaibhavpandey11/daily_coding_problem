'''
This problem was asked by Uber.
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
'''

#_________________________________________________________________________

'''
The following program takes the input from a notepad file "Election.txt".
The input data is in the format (voter_id, candidate_id)
The output is top 3 candidates if present and names of fraud voters.

For example, if the Election.txt file contains data as follows

(Madhav, Narendra Modi)
(Vinay, Narendra Modi)
(Dhruv, Narendra Modi)
(Dhruv, Manmohan Singh)
(Abhinav, Narendra Modi)
(Harsh, Bal Thackeray)
(Aditya, Manmohan Singh)
(Amit, Narendra Modi)
(Aditya, Bal Thackeray)
(Amitabh, Manmohan Singh)
(Karan, Arvind Kejriwal)
(Daya, Bal Thackeray)
(Ayush, Bal Thackeray)

Then output would be as follows

Rank 1: 'Narendra Modi'
Rank 2: 'Bal Thackeray'
Rank 3: 'Manmohan Singh'

Fraud voters: 'Aditya', 'Dhruv'
'''

with open("Election.txt", 'r') as file: str_voters_list = (file.read()).split('\n')
file.close()

voters_list, candidates_votes, fraud_voters, temp = list(), dict(), set(), dict()

for str_voters in str_voters_list:
    temp_voters_list = str_voters[1: -1].split(',')
    voters_list.append((temp_voters_list[0].strip(), temp_voters_list[1].strip()))

for (voter, candidate) in voters_list: temp[voter] = temp.get(voter, 0) + 1
for voter, count in temp.items():
    if count > 1:
        i = 0
        while i < len(voters_list):
            if voters_list[i][0] == voter:
                fraud_voters.add(voter)
                voters_list.pop(i)
            i += 1

temp.clear()
for (voter, candidate) in voters_list: temp[candidate] = temp.get(candidate, 0) + 1
for (candidate, votes) in temp.items(): candidates_votes[votes] = candidates_votes.get(votes, ()) + (candidate,) 
sorted_votes_list = sorted(candidates_votes.items(), key = lambda x: x[0], reverse = True)

for i in range(3): print("Rank %d:" %(i+1), str(sorted_votes_list[i][1]).strip('(),'))
print()
print("Fraud voters: " + str(fraud_voters).strip('{}') if len(fraud_voters) else "Fraud voters: 0")
    

