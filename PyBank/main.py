import csv

# Function to calculate the average
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return round(total / count, 2)

# Full file path to the dataset
file_path = r'C:\Users\artur\OneDrive\Escritorio\BootCamp ITESM\Challenges\Challenge 3\PyBank\Resources\budget_data.csv'


# Read the dataset file
with open('budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    data = list(csv_reader)

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Loop through the data
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
    
    # Update previous profit
    previous_profit = profit

# Calculate the average change
average_change = average(changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
