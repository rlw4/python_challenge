
num_of_rows = 0
months = 0
dates = []
profit_Loss = []
total_values = 0
avg_change = 0

max_value = 0
min_value = 0

#Import CSV data
import os
import csv

budgetCSV = os.path.join("Resources","budget_data.csv")


with open(budgetCSV) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        dates.append(row[0])
        profit_Loss.append(int(row[1]))

#    print("Total Rows:" + str(num_of_rows))
    print("Financial Analysis")
    print("------------------------------------")
    
#calculate total number of months
    months = len(dates)

    print("Total Months: "+ str(months))

#calc net total amount of Profit/losses over the entire period
for values in profit_Loss:
    total_values += int(values)

print("Total: $" + str(total_values))

#calc the changes in profit/losses over the entire period,
# then find the average of those changes
avg_change = total_values/months

print("Average Change: $" + str(round(avg_change,2)))

#greatest increase in profits (date & amount) over the entire period
max_value = max(profit_Loss)
max_index = profit_Loss.index(max_value)
max_date = dates[max_index]

print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_value) + ")")

#greatest decrease in profits (date & amount) over the entire period
min_value = min(profit_Loss)
min_index = profit_Loss.index(min_value)
min_date = dates[min_index]

print("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(min_value) + ")")

#print the analysis to the terminal
output_path = os.path.join("analysis", "PyBank_Report.txt")

txtwriter = open(output_path, "w")
txtwriter.write("Financial Analysis")
txtwriter.write("\n")
txtwriter.write("------------------------------------")
txtwriter.write("\n")
txtwriter.write("Total Months: "+ str(months))
txtwriter.write("\n")
txtwriter.write("Total: $" + str(total_values))
txtwriter.write("\n")
txtwriter.write("Average Change: $" + str(round(avg_change,2)))
txtwriter.write("\n")
txtwriter.write("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_value) + ")")
txtwriter.write("\n")
txtwriter.write("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(min_value) + ")")
txtwriter.close()
