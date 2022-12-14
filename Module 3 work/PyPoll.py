#Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# Read the header row
    headers =next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1
        # Print the canddiate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add the canddiate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that cnadiate's vote count
            candidate_votes[candidate_name]=0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name]+= 1
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------")
    print(election_results, end="")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results =(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print the candidate name and percentage of votes
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f'Winning Vote Count: {winning_count:,}\n'
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
        



