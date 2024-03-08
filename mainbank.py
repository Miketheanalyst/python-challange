
import csv
from pathlib import Path

# Path to the CSV file
file_path = Path(r'C:\Users\52614\Desktop\BootCamp Modules\Module 3\Module 3 Challenge\Excercises\PyBank\budget_data(PB).csv')

# Initialize variables
total_months = 0
net_total_amount = 0
previous_month_amount = 0
monthly_change = []
greatest_increase = ["", 0]  # Start with empty date and 0 amount
greatest_decrease = ["", float("inf")]  # Start with empty date and infinity amount

#float("inf") is used to ensure a robust positive starting value in the event where there are no negative values
#In this case the greatest_decrease would technically be the smallest increase, so infinity is used as a starting value 
#to ensure all the following values are smaller than the starting value.


# Open and read the CSV file

with open(file_path, 'r') as csvfile: # With ensures the file is closed properly ;'r' is used to open the file in read mode ; csvfile is associated with the file_path variable
    csvreader = csv.reader(csvfile) # csv.reader function from csv module is used to create a csvreader object
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader: #Iteration through the csv file where csvreader object yields rows as a list, Ive interpreted each row in collumn A to correspond to a 1 month value.
        # Count total months
        total_months += 1 # Fro each row the total_months variable is increased by 1 
        # Calculate net total amount of "Profit/Losses"
        net_total_amount += int(row[1]) # Sum of row 1 values in each iteration, complete iteration results in sum of all column values.
        
       # Calculate monthly change in "Profit/Losses"
        if total_months > 1: # >1 skips the calculation for the first row
            change = int(row[1]) - previous_month_amount # int(row[1]) is used to procure the value of the current iteration in row 1 
            monthly_change.append(change)
            
            # Check for greatest increase in profits
            if change > greatest_increase[1]: #change is evaluated against the greatest_increase list
                greatest_increase[0] = row[0] 
                greatest_increase[1] = change # greatest increase is updated if condition met 
            

        
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            
            # Check for greatest decrease in profits
            if change < greatest_decrease[1]:#change is evaluated against the greatest_decrease list
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change # greatest_decrease is update if condtion met 
        
        # Update previous month amount for next iteration's change calculation
        previous_month_amount = int(row[1]) # The value of the pre

# Calculate the average change in "Profit/Losses", avoiding division by zero error
average_change = sum(monthly_change) / len(monthly_change) if monthly_change else 0

# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

