import os
import csv
csvpath = os.path.join("election_data.csv")
#file_load = "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data (1).csv"
file_write = "HW3_Python.txt"
votes = 0
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(csvpath) as voter_data:

    reader = csv.reader(voter_data)
    header = next(reader)

    for row in reader:

        candidate_name = row[2]
        total_votes = total_votes + 1

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1    
    #print(". ", end="")
with open(file_write, "w") as txt_file:
    results = ("\n\nResults\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------\n")
    print(results, end="")
    txt_file.write(results)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentage = (float(votes) / float(total_votes)) *100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)
    winning_candidate_table = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_table)
    txt_file.write(winning_candidate_table)
    

    
        

        
