#Q1 PyBank: Total number of months in dataset

import pandas as pd

# Load your dataset into a Pandas DataFrame
df = pd.rbudget_datar_dataset.csv')

# Convert the date column to datetime format
df['Date'] = pd.to_datetime(
#Create a new column that extracts the month from each daetd['Date'])

# Create a new column for the month
df['Month'] = df['Date'].dt.month

# Count the numbe in the new columnr of unique months
num_months = df['Month'].nunique()

print("Number of unique m#onths:", num_months)
#in this code snippet:

#Replace 'your_dataset.csv' with th#e path to your dataset.
#Ensure that the date column in your dataset is named 'Date' or modi#fy the code accordingly.
#The dt.month method extracts #the month from each date.
#The nunique() method counts the number of uni#que months in the dataset.
#This code will help you determine the number of unique months present in your dataset based on the column of consecutive dates.