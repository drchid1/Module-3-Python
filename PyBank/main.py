
# Importing of required modules
import pandas as pd

# Creating the dataframe form the csv file in resources folder
df = pd.read_csv("Resources/budget_data.csv")

# Calculation of the total number of months - each row is a new month
tot_months = len(df.index)

# Calculation of the net total amount of "Profit/Losses"
tot_amount = df['Profit/Losses'].sum()

# Calculation of the average of changes
# Declaration of new variables & list
change_list = []
change_list_records = len(df.index) - 1

# Loop to calculate the change in "Profit/Losses" and saving it in new list
for index in range(change_list_records):
    change = df.iloc[index+1,1] - df.iloc[index,1]
    new_record = df.iloc[index+1,0], change
    change_list.append(new_record)


# Making the new list into a dataframe for analysis
dfc = pd.DataFrame(change_list, columns = ['Date', 'Change'])

# Calculation of the average change
sum_changes = dfc['Change'].sum()
avg_change = round(sum_changes / change_list_records, 2)

# Identification of greatest increase & decrease in profits
greatest_inrease_rec = dfc['Change'].idxmax()
greatest_derease_rec = dfc['Change'].idxmin()

# Formating of the greatest increase & decrease in profits
greatest_increase = (f"{dfc.iloc[greatest_inrease_rec, 0]} (${dfc.iloc[greatest_inrease_rec, 1]})")
greatest_decrease = (f"{dfc.iloc[greatest_derease_rec, 0]} (${dfc.iloc[greatest_derease_rec, 1]})")

# Output of the Analysis
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${tot_amount}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")

# Opening of file to write to in Analysis folder
with open("Analysis/budget_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write(f"Total Months: {tot_months}\n")
    file.write(f"Total: ${tot_amount}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")
    file.close()
