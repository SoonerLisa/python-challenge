# -*- coding: UTF-8 -*-
# used kernal: dev (Python 3.10.14
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os #for building file paths

# Files to load and output (update with correct file paths)

csv_path = os.path.join("Resources", "budget_data.csv")  # Input file path
with open (csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
# Successfully store the header row - check    
    header = next(csvreader)
    print("Header", header)
    
#     #set up pre for loop
# total_months = 0 #place holders, starting values to fill[0] in print statements below
# previous_profit_loss = 0
# net_total = 0
# change=[] 

# # (python)-inf to find the smallest/ inf largest change; ultimately asking for ["date", smallest/largest change]
# greatest_increase = ["",float("-inf")]
# greatest_decrease = ["",float("inf")]

# # for loop 
# with open(csv_path,"r") as csv_file: #prepping
#     csv_reader = csv.reader(csv_file) #parsing;where the csv import dependency is first used
#     next(csv_reader) #skips header row
#     csv_data = list(csv_reader) #data converted to a list

#     for row in csv_data: #next calc the total, and then the change, the greatest increase/decrease
#         total_months+=1
#         print(row)

        
#         # Calculate change-these come from Xpert
        
#         if previous_profit_loss is not None:
#             change = current_profit_loss - previous_profit_loss
#             changes.append(change)
            
#         # Check for greatest increase/decrease
#         if change > greatest_increase[1]:
#             greatest_increase = [row[0], change]
#             if change < greatest_decrease[1]:
#                 greatest_decrease = [row[0], change]
        

# #calc average change, format
# average_change = sum(change)/len(change)
# rounded_average_change = round(average_change, 2)

# print(f"Financial Analysis")
# print(f"----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_total}")
# print(f"Average Change: ${rounded_average_change}")
# print(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}")
# print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")
# # Open a text file in write mode (text file only) use this block or the next for terminal and file output
# with open('Analysis/pybank_analysis_results.txt', 'w') as file:
#     # Write PyBank results
#     file.write(f"PyBank Financial Analysis Results\n")
#     file.write(f"Total Months: {total_months}\n")
#     file.write(f"$Total: ${net_total}\n")
#     file.write(f"Average Change: ${rounded_average_change}\n")
#     file.write(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n")
#     file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")