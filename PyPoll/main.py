import os
import csv

file_path=os.path.join("PyPoll","Resources","Homework 3_PyPoll_Resources_election_data.csv")

with open(file_path,"r") as csvfile:
    pypoll_csv=csv.reader(csvfile,delimiter=",")
    header = next(pypoll_csv)
    votes=0
    politicians=[]
    vote=[]
    percentages=[]

    for row in pypoll_csv:

        votes=votes+1

        if votes==1:
            politicians.append(row[2])
            vote.append(0)
            vote[politicians.index(row[2])] += 1

            
        elif not row[2] in politicians:
            politicians.append(row[2])
            vote.append(0)
            vote[politicians.index(row[2])] += 1
        
        else:
            vote[politicians.index(row[2])] += 1


    for i in range(len(politicians)):
        percentages.append(1)
        percentages[i]=float(vote[i])/votes*100
    
    
    winner=politicians[vote.index(max(vote))]

path="PyPoll/analysis/main.txt"
file1=open(path,"w")

file1.write("Election Results \n\n")

file1.write("--------------------------------- \n")
file1.write(f"Total Votes: {votes} \n")
file1.write("--------------------------------- \n")
for x in range(len(politicians)):
    file1.write(f"{politicians[x]}: {round(percentages[x],2)}% ({round(vote[x])}) \n")

file1.write("--------------------------------- \n")
file1.write(f"Winner: {winner} \n")
file1.write("---------------------------------")

