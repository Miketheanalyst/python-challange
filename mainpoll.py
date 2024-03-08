import csv

# Path to your CSV file
filename = (r'C:\Users\52614\Desktop\BootCamp Modules\Module 3\Module 3 Challenge\Excercises\PyPoll\election_data(PP).csv') # ¨r¨is used to indicate raw string so path can be accepted as is 


# Initialize variables
total_votes = 0 # Variable to track the number of votes
candidates = {} #Dictionary to store names as ket and vote count as value
winner = ""
max_votes = 0

# Open the CSV file
with open(filename, mode='r') as file: #With is used to properly close program once the block of code is executed
    # Create a CSV reader object
    csvreader = csv.reader(file) #csvreader is created as an object that will iterate over lines
    
    # Skip the header
    next(csvreader) #next is used to skip the header row
    
    # Process each row
    for row in csvreader:
        total_votes += 1 # Each iteration increases the value of total_votes by 1 
        candidate_name = row[2]  # Candidate names are in the third column 
        
        # If the candidate is in the dictionary, increment their vote count
        if candidate_name in candidates: #This line of code checks if the candidate´s name is in the candidates dictionary.
            candidates[candidate_name] += 1
        else:
            # Otherwise, it is added to the dictionary and the vote count increases by 1.
            candidates[candidate_name] = 1

print("Election Results")
print("---------------------------------------------------------------")

# Print total votes
print(f"Total Votes: {total_votes}\n") #\n is used to make the output easier to read.

# Print each candidate's name, vote percentage, and total votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the winner
print(f"\nWinner: {winner}")
