import csv
import os

election_path = os.path.join("PyPoll/Resources/election_data.csv")
election_path_output = ("PyPoll/Resources/election_data.txt")

votes = 0
winner_votes_total = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_choice = []
candidate_votes = {}


with open(election_path) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_choice:
            
            candidate_choice.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    # the Winner is :
    if (votes > winner_votes_total):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
    
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
# results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(),)

# Final results
print("-------------------------")
print("Winner: " + str(winner[1]))
print("-------------------------")





# Output txt Files
with open(election_path_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))