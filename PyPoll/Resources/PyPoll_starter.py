# -*- coding: UTF-8 -*-
# kernal used: dev(Python 3.10.14)

"""PyPoll Homework Starter File."""

# Import necessary modules
import pandas as pd

# Open the CSV file and process it
election_data_df = pd.read_csv(r'C:\Users\soone\python-challenge\PyPoll\Resources\election_data.csv')

# Successfully store the header row - check
print(election_data_df.columns)

# Initialize variables to track the election data
# The total # of votes each candidate won
candidate_votes = election_data_df['Candidate'].value_counts()
print (candidate_votes)

# Track the total number of votes cast
import numpy as np

candidates = np.array(["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"])
votes = np.array([85213, 272892, 11606])

# Find the index of the candidate with the most votes
winner_index = np.argmax(votes)

# Display the winner
print_winner =(f"Winner: {candidates[winner_index]}")
print(print_winner)

# Define lists and dictionaries to track candidate names and vote counts
total_votes = election_data_df['Ballot ID'].count()
candidate_votes = election_data_df['Candidate'].value_counts().sort_index()

#Percentage of votes per candidate
decimal_value = candidate_votes / total_votes
decimal_value

percentage_value = decimal_value * 100
percentage_value = pd.DataFrame({"percentage":percentage_value, "votes":candidate_votes})
percentage_value

# Winning Candidate and Winning Count Tracker
for candidate, row in percentage_value.iterrows():
    print(f"{candidate}: {round(row['percentage'],3)}% ({int(row['votes'])})")


#Clean results
print('Election Results')
print('-----------------------------')
print('Total Votes:', total_votes)
print('-----------------------------')
for candidate, row in percentage_value.iterrows():
    print(f"{candidate}: {round(row['percentage'],3)}% ({int(row['votes'])})")
print('-----------------------------')
print(print_winner)
print('-----------------------------')   

# Prepare the results (results to txt file and terminal)
with open('pypoll_analysis_results.txt', 'w') as file:
    # Write PyPoll results
    file.write(f"PyPoll Analysis Results\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"Each Candidate, Percentage of Votes, and Vote Count:\n")
    for candidate, row in percentage_value.iterrows():
        file.write(f"{candidate}: {round(row['percentage'], 3)}% ({int(row['votes'])})\n")
    file.write(f"{print_winner}\n")