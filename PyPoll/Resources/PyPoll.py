import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

###Total vote counter
total_votes = 0

### List of data
count = {}
num_of_votes = 0
candidates = []


### Open csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    line = next(csvreader, None)
    for line in csvreader:
        ### add total
        num_of_votes = num_of_votes + 1

        ##who vote was made for
        names = line[2]

        ### Tally Votes
        if names in candidates:
            count[names] += 1
        ###Make new entry    
        else:
            candidates.append(names)
            count[names] = 1
            

print("Total Votes: ",num_of_votes)

for k, v in count.items():
    print(k,":",round(v/num_of_votes*100,4),"% (",v,")")

import operator
print("Winner: ",max(count.items(), key = operator.itemgetter(1))[0])   

with open("results.txt","w",newline="\n") as txt_file:
    for k, v in count.items():
        txt_file.write(f"{k}: {round(v/num_of_votes*100,4)}% ({v})\n")
    txt_file.write(f"Total Votes: {num_of_votes}\n")
    txt_file.write(f"Winner: {max(count.items(), key = operator.itemgetter(1))[0]})")
             



 




 












