# This program makes a summary of voting data from a CSV file

# Importing of modules
import pandas as pd

# Creating of the data frame using the CSV file
df = pd.read_csv('Resources/election_data.csv')

# Calculation of the total number of votes as each row is a vote
tot_votes = len(df.index)

# Creating a list of all the candidates with thier respective vote counts
# using a list comprehension
candidate_list = [(value, count) for value, count in df['Candidate'].value_counts().items()]

# Declaration of variable and a dictionary to store candidate vote summary

max_votes = 0
output_list = {}

# Loop to calculate the percentage votes for each candidate and identification of the winner
for n in range(len(candidate_list)):
    candidate_name = candidate_list[n][0]
    candidate_votes = candidate_list[n][1]
    candidate_percent = round((candidate_votes / tot_votes) * 100, 3)

    # Creating of variables to make dictionary of candidates
    key = candidate_name
    values = {
        "votes" : eval("candidate_votes"),
        "percentage" : eval("candidate_percent")
    }
    output_list[key] = values

    # Conditional to find the winning candidate
    if candidate_votes > max_votes:
        max_votes = candidate_votes
        winning_candidate = candidate_name

# Creating of a text file and saving the results
with open ('Analysis/vote_analysis.txt', 'w') as file:

    file.write(f"Election Results\n")
    file.write("-"* 25)
    file.write(f"\nTotal Votes {tot_votes}\n")
    file.write("-" * 25)
    file.write("\n")
    for name, info in output_list.items():
        file.write(f"{name}: {info['percentage']}% ({info['votes']})\n")
    file.write("-" * 25)
    file.write(f"\nWinner: {winning_candidate}\n")
    file.write("-" * 25)

# Reading of the results file to display in the terminal
with open ('Analysis/vote_analysis.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)