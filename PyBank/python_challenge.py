import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data) as csvfile :
    csv_reader=csv.reader(csvfile)
    csv_header=next(csv_reader)
   


    Total_Months = 0
    Total = 0
    Average_change = 0
    Date = []
    Profits = []
    Previous_profit = 0
    difference = []
    Total_difference = 0
    Increase = {"Month": "", "Profits": 0}
    Decrease = {"Month": "", "Losses": 0}

    for row in csv_reader :
        Total_Months+= 1
        Total += int(row[1])
    
        Date.append(row[0])
        Profit = int(row[1])
        Profits.append(Profit)
 
        cd=0
        if Previous_profit : 0
        cd = Profit- Previous_profit
        difference.append(cd)
        Previous_profit = Profit
        
        
        if cd > Increase["Profits"]:
            Increase['Profits'] = cd
            Increase['Months'] = row[0]
        if cd < Decrease["Losses"]:
            Decrease['Losses'] = cd
            Decrease["Month"] = row[0]
    
difference.pop(0)
Average_change = sum(difference) / len(difference)

    
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${Average_change:.2f}")
print(f"Greatest Increase in Profits: {Increase['month']} ${Increase['profits']}")
print(f"Greatest Decrease in Profits: {Decrease['month']} ${Decrease['losses']}")

output = open("PyBank/Analysis/file.txt","w")
output.write(f"Financial Analysis\n")
output.write(f"----------------------------\n")
output.write(f"Total Months: {Total_Months}\n")
output.write(f"Total: ${Total}\n")
output.write(f"Average Change: ${Average_change:.2f}\n")
output.write(f"Greatest Increase in Profits: {Increase['month']} ${Increase['profits']}\n")
output.write(f"Greatest Decrease in Profits: {Decrease['month']} ${Decrease['losses']}\n")
