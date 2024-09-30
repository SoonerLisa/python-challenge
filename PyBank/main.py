# -*- coding: UTF-8 -*-
# used kernal: dev (Python 3.10.14
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
csv_path = os.path.join ("Resources","budget_data.csv")

total_months = 0 #place holders, starting values
net_total = 0
change=[] 

greatest_increase = ["",float("-inf")]
greatest_decrease = ["",float("inf")]

# for loop 
with open(csv_path,"r") as csv_file:
    csv_reader = csv.reader(csv_file) #parsing
    next(csv_reader)
    csv_data = list(csv_reader)

    for row in csv_data:
        total_months+=1
        print(row)    


average_change = sum(change)/len(change)
rounded_average_change = round(average_change, 2)
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${rounded_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")
# Open a text file in write mode (text file only) use this block or the next for terminal and file output
with open('Analysis/pybank_analysis_results.txt', 'w') as file:
    # Write PyBank results
    file.write(f"PyBank Financial Analysis Results\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"$Total: ${net_total}\n")
    file.write(f"Average Change: ${rounded_average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")