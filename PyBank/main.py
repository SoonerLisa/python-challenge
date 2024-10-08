# -*- coding: UTF-8 -*-
# kernal used: dev(Python 3.10.14)

# Dependencies
import csv
import os #for building file paths

# Open and read the csv; input csv_path
    # Successfully store the header row
csv_path = os.path.join("Resources", "budget_data.csv")
financial_analysis = os.path.join("Analysis", "financial_analysis.txt")   


with open (csv_path) as budget_data:
        csvreader = csv.DictReader(budget_data, delimiter=",")
        csv_data = list(csvreader) #data converted to a list
                   
# Initialize variables to track the budget data
total_months = len(csv_data)
total_net = 0
previous_profit_loss = None
changes = []
greatest_increase = ["",float("-inf")]
greatest_decrease = ["",float("inf")]

for row in csv_data:
        profit_loss = int(row['Profit/Losses'])
        total_net += profit_loss
        
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
        # Check for greatest increase/decrease
            if change > greatest_increase[1]:
                greatest_increase = [row['Date'], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row['Date'], change]
        
        previous_profit_loss = profit_loss

# Calc average change; Format
average_change = sum(changes)/len(changes) if changes else 0
rounded_average_change = round(average_change, 2)

# Print to terminal
print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${rounded_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#Print to text file
with open(financial_analysis, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${rounded_average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

