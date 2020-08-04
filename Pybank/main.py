import csv
import os

file_to_analyze='Resources/budget_data.csv'
file_to_output='Analysis/budget_analysis.text'

with open(file_to_analyze) as csvfile:
    reader= csv.DictReader(csvfile)

    total_months=0
    total_rev=0
    prev_rev=0
    rev_change=0
    rev_change_list=[]
    months=[]
    monthly_rev_change =[]
    greatest_decrease=0
    greatest_increase=0
    
    for row in reader:
        total_months += 1
        total_rev += int(row["Profit/Losses"])

   
        rev_change = int(row["Profit/Losses"])-prev_rev
        prev_rev = int(row["Profit/Losses"])
        rev_change_list.append((rev_change))
        months.append(row["Date"])



    for i in range (len(total_rev)-1):
        rev_change_list.append(total_rev[i+1]-total_rev[i])

        greatest_increase = max(monthly_rev_change)
        greatest_decrease = min(monthly_rev_change)


        max_increase_month=monthly_rev_change.index(max(monthly_rev_change))+1
        min_increase_month=monthly_rev_change.index(min(monthly_rev_change))+1





    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_rev}')
    print(f'Average Change: ${round(sum(rev_change_list)/(total_months)}')
    print(f'Greatest Increase in Profits: {total_months[max_increase_month]}(${ str((max_increase_month))})')
    print(f'Greatest Decrease in Profits: {total_months[min_increase_month]}(${ str((max_increase_month))})')