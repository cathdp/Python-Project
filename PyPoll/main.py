import csv
import os

file_to_analyze='election_data.csv'
file_to_output= "election_day_analysis.txt"

total_votes=[]
list_candidates []
percent_votes=[]
num_votes=0


with open(file_to_analyze) as csvfile:
    reader= csv.DictReader(csvfile)

    for row in cvsreader:
     num_votes += 1








print ("Election Results")
print ("_____________________________")
print (f'total_votes: {num_votes}')
