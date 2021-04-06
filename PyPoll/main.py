
votes = 0
voter_ids = []
county = []
candidates = []

#Import CSV data
import os
import csv

pollCSV = os.path.join("Resources","election_data.csv")


with open(pollCSV) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        voter_ids.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        votes += 1


#   print Analysis
    print("Election Results")
    print("------------------------------------")


    
#calculate total number of votes
    print("Total Votes: "+ str(votes))
    print("------------------------------------")

#make list of candidates
set_of_candidates = set(candidates)
list_of_candidates = list(set_of_candidates)

#percentage won for each candidate
votes_counts = []

for name in list_of_candidates:
    vote_counter = 0
    for vote in candidates:
        if vote == name:
            vote_counter += 1
    votes_counts.append(vote_counter)

name_index = 0
for entry in votes_counts:
    percent = '{:.3%}'.format(entry/votes)
    print(list_of_candidates[name_index] + ": " + str(percent) + " (" + str(votes_counts[name_index]) + ")")
    name_index += 1


#declare winner
print("----------------------------------------")
winner = list_of_candidates[votes_counts.index(max(votes_counts))]
print("Winner: " + winner)
print("----------------------------------------")

#print the analysis to the terminal
output_path = os.path.join("analysis", "PyPoll_Report.txt")

txtwriter = open(output_path, "w")
txtwriter.write("Election Results")
txtwriter.write("\n")
txtwriter.write("------------------------------------")
txtwriter.write("\n")
txtwriter.write("Total Votes: "+ str(votes))
txtwriter.write("\n")
txtwriter.write("------------------------------------")
txtwriter.write("\n")
namee_index = 0
for entry in votes_counts:
    percent = '{:.3%}'.format(entry/votes)
    txtwriter.write(list_of_candidates[namee_index] + ": " + str(percent) + " (" + str(votes_counts[namee_index]) + ")")
    txtwriter.write("\n")
    namee_index += 1
txtwriter.write("------------------------------------")
txtwriter.write("\n")
txtwriter.write("------------------------------------")
txtwriter.write("\n")
txtwriter.write("Winner: " + winner)
txtwriter.write("\n")
txtwriter.write("------------------------------------")
txtwriter.close()
