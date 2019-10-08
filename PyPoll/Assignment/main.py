#main.py PyPoll

import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Open and read csv
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    total_votes = 0
    canidates = []

    
    
    # Read through each row of data after the header
    for row in csvreader:
        # print(row)
        total_votes += 1
        canidates.append(row[2])
      
        
     
    #count votes for each canidate    
    Khan_votes = canidates.count("Khan")
    Correy_votes = canidates.count("Correy")  
    Li_votes = canidates.count("Li")  
    Otooley_votes = canidates.count("O'Tooley")

    #calculate percentage of votes for each canidate
    Khan_percentage = Khan_votes / total_votes
    Correy_percentage = Correy_votes / total_votes
    Li_percentage = Li_votes / total_votes
    Otooley_percentage = Otooley_votes / total_votes  

    #determine number of unique candidates
    unique_canidates = set(canidates)
    unique_canidates_count = len(unique_canidates)
    #print(f"Unique Canidates: {unique_canidates}")
    #print(f"Unique Canidates Count: {unique_canidates_count}")

    print("Election Results")
    print("----------------------------------")    
    print(f"Total Votes:  {total_votes}")
    print("----------------------------------")
    print(f"Khan: {Khan_percentage:.3%} ({Khan_votes})")
    print(f"Correy: {Correy_percentage:.3%} ({Correy_votes})")
    print(f"Li: {Li_percentage:.3%} ({Li_votes})")
    print(f"O'Tooley: {Otooley_percentage:.3%} ({Otooley_votes})")
    print("----------------------------------") 
    print("Winner: Khan")
    print("----------------------------------") 


 # Specify the file to write to
output_path = os.path.join("..", "output", "PyPoll_Output_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow([csv_header])

    # Write the financial Analysis Results
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow([f'Total Votes:   {total_votes}'])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow([f'Khan:  {Khan_percentage:.3%} ({Khan_votes})'])
    csvwriter.writerow([f'Correy:  {Correy_percentage:.3%} ({Correy_votes})'])
    csvwriter.writerow([f'Li:  {Li_percentage:.3%} ({Li_votes})'])
    csvwriter.writerow([f"O'Tooley:  {Otooley_percentage:.3%} ({Otooley_votes})"])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(['Winner:  Khan'])
    csvwriter.writerow(['------------------------------------'])
    
