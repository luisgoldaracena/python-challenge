import os
import csv

file_path=os.path.join("PyBank","Resources","Homework 3_PyBank_Resources_budget_data.csv")

with open(file_path, 'r') as pybank_csv:

    pybank_reader=csv.reader(pybank_csv,delimiter=",")
    header = next(pybank_reader)
    change=0
    acum_change=0
    months=0
    total=0
    

    for row in pybank_reader:
        
        months = months + 1
        total = total + float(row[1])
        
        if months >= 2:
            change=float(row[1])-actual_value
            acum_change=acum_change+change

        actual_value=float(row[1])

        if months == 1:
            max_valuechange=0
            max_month=row[0]
            min_valuechange=0
            min_month=row[0]

        if float(change) > max_valuechange:
            max_valuechange=float(change)
            max_month=row[0]

        if float(change) < min_valuechange:
            min_valuechange=float(change)
            min_month=row[0]


    mean_change=acum_change/(months-1)


path="PyBank/analysis/main.txt"

file1=open(path,"w")

file1.write("Financial Analysis \n\n")

file1.write("-------------------------------------------------------- \n\n")

file1.writelines(f"Total months: {months} \nTotal: ${round(total)} \nAverage Change: ${round(mean_change,2)} \nGreatest Increase in Profits: {max_month} (${round(max_valuechange)}) \nGreatest Decrease in Profits: {min_month} (${round(min_valuechange)})")

