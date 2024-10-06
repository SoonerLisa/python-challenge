# -*- coding: UTF-8 -*-
# kernal used: dev(Python 3.10.14)

"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os
from collections import defaultdict
# Open the CSV file and process it
csv_path = os.path.join("Resources", "election_data.csv")
with open (csv_path, mode='r') as csv_file:
        csvreader = csv.DictReader(csv_file, delimiter=",")
        election_data=list(csvreader)

total_votes = 0
each_candidate_votecount = defaultdict(int)

for row in election_data:
    total_votes += 1
    candidate = row('Candidate')
    each_candidate_votecount[candidate] += 1

print(f"Total Votes: {total_votes}")

for candidate, vote_count in each_candidate_votecount.items():
    print(f"{candidate}: {vote_count} votes")

#     print
#     candidates.append(row['Candidate'])


# each_candidate_votecount = defaultdict(int)

# election_data=['Candidate']
# each_candidate_votecount[candidates] += 1
# for candidates, total_votes in each_candidate_votecount.items():
#       print(f"{candidates}: {total_votes} total_votes")

 #for row in election_data:
            #total_votes += 1
# Successfully store the header row - check    
        #next(csvreader)
        #election_data=list(csvreader)
       # total_votes = 0
        #Ballot ID = {i,1}
        #list.count('Ballot ID')        
        # for Ballot ID in election_data:
        # if Ballot ID in total_votes:
#total_votes = count('Ballot ID')
# # The total # of votes each candidate won
# candidate_votes = election_data['Candidate'].value_counts()
# print (candidate_votes)

# total_votes = election_data_df['Ballot ID'].count()
# candidate_votes = election_data_df['Candidate'].value_counts().sort_index()

# election_data = csv_file
# print(election_data)
# Using f-strings:
# percentage_value = 27.6
# formatted_percentage = f"{percentage_value:.2f}%"
# print(formatted_percentage)
# Using the format() method:
# percentage_value = 27.6
# formatted_percentage = "{:.2f}%".format(percentage_value)
# print(formatted_percentage)
#
# Both of these methods will correctly format 27.6 as 27.60%.
# with open(csv_path,"r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     csv_data=list(csv_reader)
# print(csv_data)
# decimal_value = 0.276
# percentage_value = decimal_value * 100
# formatted_percentage = f"{percentage_value:.2f}%"
# print(formatted_percentage)

#Initialize variables to track the election data


# # Track the total number of votes cast
# import numpy as np

# candidates = np.array(["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"])
# votes = np.array([85213, 272892, 11606])

# # Find the index of the candidate with the most votes
# winner_index = np.argmax(votes)

# # Display the winner
# print_winner =(f"Winner: {candidates[winner_index]}")
# print(print_winner)

# # Define lists and dictionaries to track candidate names and vote counts
# total_votes = election_data_df['Ballot ID'].count()
# candidate_votes = election_data_df['Candidate'].value_counts().sort_index()

# #Percentage of votes per candidate
# decimal_value = candidate_votes / total_votes
# decimal_value

# percentage_value = decimal_value * 100
# percentage_value = pd.DataFrame({"percentage":percentage_value, "votes":candidate_votes})
# percentage_value

# # Winning Candidate and Winning Count Tracker
# for candidate, row in percentage_value.iterrows():
#     print(f"{candidate}: {round(row['percentage'],3)}% ({int(row['votes'])})")


# #Clean results
# print('Election Results')
# print('-----------------------------')
# print('Total Votes:', total_votes)
# print('-----------------------------')
# for candidate, row in percentage_value.iterrows():
#     print(f"{candidate}: {round(row['percentage'],3)}% ({int(row['votes'])})")
# print('-----------------------------')
# print(print_winner)
# print('-----------------------------')   

# # Prepare the results (results to txt file and terminal)
# with open('pypoll_analysis_results.txt', 'w') as file:
#     # Write PyPoll results
#     file.write(f"PyPoll Analysis Results\n")
#     file.write(f"Total Votes: {total_votes}\n")
#     file.write(f"Each Candidate, Percentage of Votes, and Vote Count:\n")
#     for candidate, row in percentage_value.iterrows():
#         file.write(f"{candidate}: {round(row['percentage'], 3)}% ({int(row['votes'])})\n")
#     file.write(f"{print_winner}\n")