# -*- coding: UTF-8 -*-
# used kernal: dev (Python 3.10.14
"""PyBank Homework Starter File."""

# Dependencies
import pandas as pd
import csv
import os

# Files to load and output (update with correct file paths)
csv_path = os.path.join (r'C:\Users\soone\python-challenge\PyBank\Resources', 'budget_data.csv')
df = pd.read_csv(csv_path)

print(df.columns)

total_months = len(df) - 1 + 1
print(f"Total Months: {total_months}")

net_total = df['Profit/Losses'].sum()
print(f"Total: ${net_total}")

data = pd.read_csv(r'C:\Users\soone\python-challenge\PyBank\Resources\budget_data.csv')
print(data)

df['change'] = df['Profit/Losses'].diff()
df['change'] = df['change'].fillna(0)
df['change'] = df['change'].astype(int)
df

#The changes in "Profit/Losses" over the entire period (previous cell)...
#now the average over the entire period
#the 1: consider all rows except the first one w/no change
average_change = df.loc[1:,'change'].mean()
average_change
#print(average_change)
#now round
rounded_average_change = round(average_change, 2)
print(f"Average Change: ${rounded_average_change}")

#compiling results for print once initiated
# print(f"Total Changes: {net_total}")
# print(f"Greatest Increase in Profits: {change}")
# print(f"Greatest Decrease in Profits: {change}")
# total_changes = df['change'].sum()
# print(df)
# print(f"Greatest Increase in Profits: {greatest_increase_row['Date']} ${greatest_increase_row['change']}")
# print(f"Greatest Decrease in Profits: {greatest_decrease_row['Date']} ${greatest_decrease_row['change']}")

missing_values = df['Profit/Losses'].isnull().sum()
print (missing_values)

greatest_increase_row = df.loc[df['change'].idxmax()]
greatest_decrease_row = df.loc[df['change'].idxmin()]
print(greatest_increase_row)
print(greatest_decrease_row)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${rounded_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_row['Date']} ${greatest_increase_row['change']}")
print(f"Greatest Decrease in Profits: {greatest_decrease_row['Date']} ${greatest_decrease_row['change']}")

# Open a text file in write mode (text file only) use this block or the next for terminal and file output
with open('pybank_analysis_results.txt', 'w') as file:
    # Write PyBank results
    file.write(f"PyBank Financial Analysis Results\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"$Total: ${net_total}\n")
    file.write(f"Average Change: ${rounded_average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_row['Date']} ${greatest_increase_row['change']}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_row['Date']} ${greatest_decrease_row['change']}")