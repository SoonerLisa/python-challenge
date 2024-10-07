# -*- coding: UTF-8 -*-
# kernal used: dev(Python 3.10.14)

# Import necessary modules
import csv
import os
from collections import defaultdict
import numpy as np

# Open the CSV file and process it
# Successfully store the header row
csv_path = os.path.join("Resources", "election_data.csv")
with open (csv_path, mode='r') as csv_file:
        csvreader = csv.DictReader(csv_file, delimiter=",")
        election_data=list(csvreader)
# Initialize variables to trach the election data

# The total number of votes and votes per candidate:
total_votes = 0
each_candidate_votecount = defaultdict(int)

for row in election_data:
    total_votes += 1
    candidate = row['Candidate']
    each_candidate_votecount[candidate] += 1

# Print the election results
print('Election Results')
print('-----------------------------')
print(f"Total Votes: {total_votes}")
print('-----------------------------')

# Calculate and print each candidate's results
# Print candidate, percentage, and vote count
for candidate, vote_count in each_candidate_votecount.items():
    percentage = (vote_count / total_votes) * 100  # Calculate percentage
    formatted_percentage = f"{percentage:.3f}%"  # Format to three decimal places
    print(f"{candidate}: {formatted_percentage} ({vote_count})") 

# Determine the winner
vote_counts = list(each_candidate_votecount.values())  # Get a list of vote counts
winner_index = np.argmax(vote_counts)  # Get the index of the candidate with the most votes
winner = list(each_candidate_votecount.keys())[winner_index] # Get the winner candidate's name

# Open the text file for writing
with open('pypoll_analysis_results.txt', 'w') as file:
    # Write PyPoll results
    file.write('Election Results\n')
    file.write('-----------------------------\n')
    file.write(f"Total Votes: {total_votes}\n")
    file.write('-----------------------------\n')

    # Calculate and write each candidate's results to the text file
    for candidate, vote_count in each_candidate_votecount.items():
        percentage = (vote_count / total_votes) * 100  # Calculate percentage
        formatted_percentage = f"{percentage:.3f}%"  # Format to three decimal places
        file.write(f"{candidate}: {formatted_percentage} ({vote_count})\n")  # Write candidate, percentage, and vote count

    # Write the winner to the text file
    file.write('-----------------------------\n')
    file.write(f"Winner: {winner}\n")
    file.write('-----------------------------\n')