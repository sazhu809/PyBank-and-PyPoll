import os 
import csv

budget_data = os.path.join(".", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next (csvreader)

    numMonth = 0
    profit_losses = 0
    total_change = 0
    previous = 0
    avg = 0
    greatest_profit = 0
    greatest_month = ""
    decrease_profit = 0
    decrease_month = ""
    
    

    for row in csvreader:
        numMonth += 1
        profit_losses = profit_losses + int(row[1])
        current = int(row[1])
        

        if numMonth > 1:
            change = current - previous
            total_change += change 

            if change > greatest_profit:
                greatest_profit = change
                greatest_month = row[0]

            if change < decrease_profit:
                decrease_profit = change
                decrease_month = row[0]

        previous = current

    avg = total_change / (numMonth - 1)


    print("Financial Analysis")
    print("---------------------------------------------")
    print(f'Total of months: {numMonth}')
    print(f'Total: ${profit_losses}')
    print(f'Average Change: ${avg}')
    print(f'Greatest Increase in Profits: {greatest_month} {greatest_profit}')
    print(f'Greatest Decrease in Profits: {decrease_month} {decrease_profit}')
    
