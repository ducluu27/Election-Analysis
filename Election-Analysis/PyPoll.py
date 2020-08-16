#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of cotes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#Assign a variable for the file to load and the path
#file_to_load = 'election_results.csv'
#Open the election results and read the file
#with open(file_to_load) as election_data:
#To do: perform analysis
    #print(election_data)
#close the file
#election_data.close()
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to load a file from a path
file_to_save = os.path.join("analysis","election_analysis.txt")
#1. Initialize a total vote counter
total_votes = 0
#Candidate options
candidate_options = []
#declare the empy dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open the election results and read the file
with open(file_to_load) as election_data:
#to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    #read the header row:
    headers = next(file_reader)
    #print the file object
    #print(election_data)
    #print each row in the csv file
    for row in file_reader:
        #Add to the total vote count:
        total_votes += 1
    #print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] +=1
#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    #determinte the percentage of votes for each candidate by looping through the counts
    #1 Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2 Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3 calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4 Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #print each candidate, their voter count and percentage to the terminal
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)
        #To do: print out each candidate's name, vote count, and percentage of votes
        #vote to the terminal
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determing winning count of candidate
    #1 determinte if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
    #2 if true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
    #3 set the winning_candidate equal to the candidate's name
            winning_percentage = vote_percentage        
#Print the winning candidates' results to the terminal
    winning_candidate_summary = (
        f"-------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)
#save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
#print the candidate vote dictionary
#print(candidate_votes)
        #print(row)
    #read and print the header row
    #headers = next(file_reader)
    #for row in file_reader:
        #2. add to the total vote count
        #total_votes += 1
        #Print the candidate name from each row
        #candidate_name = row[2]
        #if the candidate does not match any existing candidate...
        #if candidate_name not in candidate_options:
            #add it to the lsit of candidates
            #candidate_options.append(candidate_name)
        #add the candidate name to the candidate list
        #candidate_options.append(candidate_name)
        #print(row)
#print the candidate list
#print(candidate_options)
#3 Print the total votes
#print(total_votes)
#create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis","election_analysis.txt")
#using the with statement open the file as a text file
#outfile = open(file_to_save,"w")
#with open(file_to_save,"w") as txt_file:
#write some data to the file
#outfile.write("Counties")
#    txt_file.write("Arapahoe, ")
#   txt_file.write("Denver, ")
#    txt_file.write("Jefferson")
#write three counties to the file
    #txt_file.write("Arapahoe\nDenver\nJefferson")
#close the file
#outfile.close()