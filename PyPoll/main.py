# -*- coding: UTF-8 -*-
# kernal used: dev(Python 3.10.14)

# Import necessary modules
import csv
import os
from collections import defaultdict
import numpy as np

# Open the CSV file and process it
# Successfully store the header row
# Initialize variables to track the election data
csv_path = os.path.join("Resources", "election_data.csv")
election_results = os.path.join("Analysis", "election_results.txt")   

with open (csv_path, mode='r') as csv_file:
        csvreader = csv.DictReader(csv_file, delimiter=",")
        election_data=list(csvreader)

# The total number of votes per candidate:
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
    # Get a list of vote counts
    # Get the index of the candidate with the most votes
    # Get the winner candidate's name
vote_counts = list(each_candidate_votecount.values()) 
winner_index = np.argmax(vote_counts)  
winner = list(each_candidate_votecount.keys())[winner_index]
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Print to text file
with open(election_results, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-----------------------------\n")
    
    # Write each candidate's results to the text file
    for candidate, vote_count in each_candidate_votecount.items():
        percentage = (vote_count / total_votes) * 100  # Calculate percentage
        formatted_percentage = f"{percentage:.3f}%"  # Format to three decimal places
        text_file.write(f"{candidate}: {formatted_percentage} ({vote_count})\n")
    
    text_file.write("-----------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-----------------------------\n")