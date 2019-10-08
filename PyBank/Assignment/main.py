#main.py PyBank

import os
import csv

#budget_data_csv = open(r"C:\Users\ca25935\Desktop\UCD Data Analytics\Homework\Homework #3\PyBank\Resources\budget_data.csv",encoding='utf8')

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')


# Open and read csv
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    total_months = 0
    Net_total_ProfitsLosses = 0
    avgChange = 0.0
    CurrProfit = 0.0
    PrevProfit = 0.0
    greatestIncrease = 0.0
    GI_MonthYear = "MMM-YYYY"
    greatestDecrease = 0.0
    GD_MonthYear = "MMM-YYYY"
    
    # Read through each row of data after the header
    for row in csvreader:
        # print(row)
        total_months += 1
        
        Net_total_ProfitsLosses += int(row[1])
        #track average of changes
        if total_months == 1:
            CurrProfit = float(row[1])
            
        if total_months >= 2:
            PrevProfit = CurrProfit
            CurrProfit = float(row[1])
            avgChange += (CurrProfit - (PrevProfit))
            #to view the row and data elements
            #print(f"{row[0]} {CurrProfit} {PrevProfit} {avgChange}")
           
            #Track the greatest increase and the greatest decrease
            #set the values for comparison
            if total_months == 2:
                greatestIncrease = avgChange
                GI_MonthYear = str(row[0])
                greatestDecrease = avgChange
                GD_MonthYear = str(row[0])
            #compare existing values for greatest increase and greatest decrease
            if (CurrProfit - PrevProfit) > greatestIncrease:
                greatestIncrease = (CurrProfit - PrevProfit)
                GI_MonthYear = str(row[0])
            if (CurrProfit - PrevProfit) < greatestDecrease:
                greatestDecrease = (CurrProfit - PrevProfit)
                GD_MonthYear = str(row[0])
        
        
    #calculate the average of changes in profits/losses        
    avgChange = avgChange / (total_months - 1)
        # total_months += int(budget.count(row[0])+5)
        #total_months += int(months)
    

    print("Financial Analysis")
    print("----------------------------------")    
    print(f"Total Months: {total_months}")
    print(f"Total: ${Net_total_ProfitsLosses}")
    print(f"Average Change: ${avgChange:.2f}")
    print(f"Greatest Increase in Profits: {GI_MonthYear}  (${greatestIncrease:.0f})")
    print(f"Greatest Decrease in Profits: {GD_MonthYear}  (${greatestDecrease:.0f})")
    

    # Specify the file to write to
output_path = os.path.join("..", "output", "PyBank_Output_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow([csv_header])

    # Write the financial Analysis Results
    csvwriter.writerow(['Statistical Analysis'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total: ${Net_total_ProfitsLosses}'])
    csvwriter.writerow([f"Average Change: ${avgChange:.2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {GI_MonthYear}  (${greatestIncrease:.0f})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {GD_MonthYear}  (${greatestDecrease:.0f})"])


