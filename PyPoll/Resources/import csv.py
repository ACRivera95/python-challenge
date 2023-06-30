import csv

file_path = "C:/Users/artur/OneDrive/Escritorio/BootCamp ITESM/Challenges/Challenge 3/PyPoll/Resources/election_data.csv"


total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header so we start reading the data 
    header = next(csvreader)

    # move trough all the table
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate name from the row
        candidate = row[2]

        # If the candidate is not already in the candidates dictionary, add them
        if candidate not in candidates:
            candidates[candidate] = 0

        # Increment the vote count for the candidate
        candidates[candidate] += 1

# Create a variable to store the analysis results
analysis_results = []


analysis_results.append("Election Results")
analysis_results.append("-------------------------")
analysis_results.append(f"Total Votes: {total_votes}")
analysis_results.append("-------------------------")

# Iterate over the candidates and calculate percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100

    # Append the candidate's name, percentage of votes, and total votes to the analysis results
    analysis_results.append(f"{candidate}: {percentage:.3f}% ({votes})")

    # Check which candidate is winning 
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Determine the winner 
analysis_results.append("-------------------------")
analysis_results.append(f"Winner: {winner}")
analysis_results.append("-------------------------")

# Print the analysis results to the terminal
for result in analysis_results:
    print(result)

output_file_path = "C:/Users/artur/OneDrive/Escritorio/BootCamp ITESM/Challenges/Challenge 3/PyPoll/Resources/election_results.txt"

with open(output_file_path, 'w') as file:
    for result in analysis_results:
        file.write(result + "\n")

print(f"The analysis has been exported to {output_file_path}.")