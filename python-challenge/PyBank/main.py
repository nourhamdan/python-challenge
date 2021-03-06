import csv
import os

# path to collect data
budget_path = os.path.join(PyBank/Resources/budget_data.csv")
budget_path_output = ("PyBank//Resources/budget_data.txt")

# Variables to Track
total_months = 0
total_revenue = 0

prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

profit_loss_changes = []

# Read Files
with open(budget_path) as csvfile:
    reader = csv.DictReader(csvfile)

    #loop through rows to add up the total months/profit losses 
    for row in reader:

        
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        print(row)

        # Keep track of changes
        profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        print(profit_loss_change)

        # Reset the value of prev_profit_loss to the complete row 
        prev_profit_loss = int(row["Profit/Losses"])
        print(prev_profit_loss)

        # Find the results of  the greatest increase
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[1] = profit_loss_change
            greatest_increase[0] = row["Date"]

        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[1] = profit_loss_change
            greatest_decrease[0] = row["Date"]

        # Add to the profit_loss_changes list
        profit_loss_changes.append(int(row["Profit/Losses"]))

    # create the profit loss average
    profit_loss_avg = sum(profit_loss_changes) / len(profit_loss_changes)
    
    # Show Output
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total : " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    


# Output txt Files
with open(budget_path_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")