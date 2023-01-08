import os 
import csv

election_data = os.path.join(".", "Resources", "election_data.csv")
election_out = os.path.join(".", "analysis", "election_analysis.txt")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    total_votes = 0
    cdd = []
    num_votes = []
    percent_votes = []
    winner = ""


    for row in csvreader:
        total_votes +=1

        if row[2] not in cdd:
            cdd.append(row[2])
            i = cdd.index(row[2])
            num_votes.append(1)
        else:
            i = cdd.index(row[2])
            num_votes[i] += 1
    
for votes in num_votes:
    percent = round((votes/total_votes) * 100,2)
    percent_votes.append(percent)
    
# winner_votes = max(num_votes)
# winner_index = num_votes.index(winner_votes)
# winner = cdd[winner_index]

winner = cdd[num_votes.index(max(num_votes))]

with open(election_out,"w") as txtfile:

    output_header = (
        f'\nElection Results \n'
        f'---------------------------------------------\n'
        f'Total Votes: {total_votes}\n'
        f'---------------------------------------------\n'
    )



    
    print(output_header)
    txtfile.write(output_header)

    for i in range(len(cdd)):
        print(f'{cdd[i]} : {percent_votes[i]}% ({num_votes[i]}) ')
        txtfile.write(f'{cdd[i]} : {percent_votes[i]}% ({num_votes[i]})\n')

    
    output_body = (
        f'---------------------------------------------\n'
        f'Winner: {winner}\n'
        f'---------------------------------------------\n'
    )

    print(output_body)
    txtfile.write(output_body)

    




        
