#First import os module
import os
#Import module for reading csv files
import csv
#set path for file
csvpath = os.path.join('..', 'PyPoll','Resources2', "election_data.csv") 
#set text file output
text_path = "Final_Analysis.txt"
outfile = os.path.join('analysis', text_path)

# Open the CSV file
with open(csvpath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # The total number of votes cast (row count after the header)
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # Create new list from CSV column "C" to get a list of candidates that received votes
    cand_list = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in cand_list: 
            cand_list.append(candidate)
    cand_count = len(cand_list)

  # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = list()
    percentage = list()
    for j in range (0,cand_count):
        name = cand_list[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # The winner of the election based on popular vote.
    winner = votes.index(max(votes))    

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
  # Print the results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,cand_count): 
        print(f"{cand_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {cand_list[winner]}")
    print("----------------------------")

  # Print the results to "PyPoll.txt" file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,cand_count): 
        print(f"{cand_list[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {cand_list[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))