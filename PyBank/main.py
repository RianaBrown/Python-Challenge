#First import os module
import os
#Import module for reading csv files
import csv
#set path for file
csvpath = os.path.join('..', 'PyBank','Resources', "budget_data.csv") 
#set text file output
text_path = "Final_Analysis.txt"
outfile = os.path.join('analysis', text_path)
#set variables
totalmonths = []
profits = []
profit_loss_change = 0
pc = []
greatest_increase = ["", float("-inf")]
greatest_decrease = ["", float("inf")]
# use csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile) #, delimiter=',')
    csv_header = next(csvreader)
    #print(f"csv header: {csv_header})
    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))
for i in range(len(profits)-1):
        profit_loss_change = profits[i+1] - profits[i]
        pc.append(profit_loss_change)
        if profit_loss_change > greatest_increase[1]:
             greatest_increase[1] = profit_loss_change
             greatest_increase[0] = totalmonths[i+1]
        if profit_loss_change < greatest_decrease[1]:
             greatest_decrease[1] = profit_loss_change
             greatest_decrease[0] = totalmonths[i+1]

total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = (sum(pc) / len(pc))
# greatest_increase = ((totalmonths[profit_loss_change.index(max(profit_loss_change))+1]))
# gp_increase = max(profit_loss_change)
# gp_decrease = max(profit_loss_change)
print("Financial Analysis")
print("----------------------------")
# The total number of months 
print(f"Total Months: {total_months}")
# The net total amount of "Profit/Losses" 
print(f"Total: ${sum_profits}")
# The changes in "Profit/Losses" over the entire period, and average of changes
print(f"Average Change: ${avg_change:.2f}")
# The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
# The greatest decrease in profits (date and amount) over the entire period
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

                


