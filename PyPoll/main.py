# Eric Messerich
# HW #3

import pandas as pd
import os

file_path = os.path.join("Resources","election_data.csv")

f = file("Election_Results.txt", "w")

df = pd.read_csv(file_path)

print >> f,("Eric Messerich")
print >> f,("Data Analytics Cohort 3")
print >> f,("HW #3")
print >> f,("")

total_votes = len(df["Voter ID"].value_counts())
print("-----------------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------------")

print >> f,("-----------------------------------")
print >> f,("Total Votes: " + str(total_votes))
print >> f,("-----------------------------------")

total_votes = float(total_votes)

Khan_votes_df = df.loc[df["Candidate"] == "Khan", :]
Khan_votes = len(Khan_votes_df["Voter ID"].value_counts())
Khan_percent = Khan_votes/total_votes * 100
Khan_percent = round(Khan_percent,3)
print("Khan: " + str(Khan_percent) + "% (" + str(Khan_votes) + ")")
print >> f,("Khan: " + str(Khan_percent) + "% (" + str(Khan_votes) + ")")

Correy_votes_df = df.loc[df["Candidate"] == "Correy", :]
Correy_votes = len(Correy_votes_df["Voter ID"].value_counts())
Correy_percent = Correy_votes/total_votes * 100
Correy_percent = round(Correy_percent,3)
print("Correy: " + str(Correy_percent) + "% (" + str(Correy_votes) + ")")
print >> f,("Correy: " + str(Correy_percent) + "% (" + str(Correy_votes) + ")")

Li_votes_df = df.loc[df["Candidate"] == "Li", :]
Li_votes = len(Li_votes_df["Voter ID"].value_counts())
Li_percent = Li_votes/total_votes * 100
Li_percent = round(Li_percent,3)
print("Li: " + str(Li_percent) + "% (" + str(Li_votes) + ")")
print >> f,("Li: " + str(Li_percent) + "% (" + str(Li_votes) + ")")

OTooley_votes_df = df.loc[df["Candidate"] == "O'Tooley", :]
OTooley_votes = len(OTooley_votes_df["Voter ID"].value_counts())
OTooley_percent = OTooley_votes/total_votes * 100
OTooley_percent = round(OTooley_percent,2)
print("O'Tooley: " + str(OTooley_percent) + "% (" + str(OTooley_votes) + ")")
print("-----------------------------------")
print >> f,("O'Tooley: " + str(OTooley_percent) + "% (" + str(OTooley_votes) + ")")
print >> f,("-----------------------------------")

vote_results = [{"Candidate":"Khan", "Total Votes": Khan_votes},
                {"Candidate":"Correy", "Total Votes": Correy_votes},
                {"Candidate":"Li", "Total Votes": Li_votes},
                {"Candidate":"OTooley", "Total Votes": OTooley_votes}]

vote_results_df = pd.DataFrame(vote_results)
vote_results_df = vote_results_df.sort_values("Total Votes", ascending=False)
vote_results_df = vote_results_df.reset_index()
Winner = vote_results_df.loc[0,"Candidate"]

print("Winner: " + str(Winner))
print("-----------------------------------")
print >> f,("Winner: " + str(Winner))
print >> f,("-----------------------------------")

f.close()
