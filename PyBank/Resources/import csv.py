import csv


def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return round(total / count, 2)


file_path = r'C:\Users\artur\OneDrive\Escritorio\BootCamp ITESM\Challenges\Challenge 3\PyBank\Resources\budget_data.csv'


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  
    data = list(csv_reader)

# variables needed for all the outcomes
total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# move trough the csv file
for row in data:
    # Extract the values
    date = row[0]
    profit = int(row[1])
    
    # Calculate total months and net total
    total_months += 1
    net_total += profit
    
    # Calculate the change in profit
    change = profit - previous_profit
    if previous_profit != 0:
        changes.append(change)
    
    # Update greatest increase and decrease
    if change > greatest_increase[1]:
        greatest_increase = [date, change]
    if change < greatest_decrease[1]:
        greatest_decrease = [date, change]
    
    # Update profit
    previous_profit = profit


average_change = average(changes)

analysis_summary = f'''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})'''


print(analysis_summary)

# Export the results to a text file
output_file = 'financial_analysis.txt'
with open(output_file, 'w') as file:
    file.write(analysis_summary)

print(f"The analysis has been exported to {output_file}.")