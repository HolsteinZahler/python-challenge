# Import the os module to create file paths across operating systems
import os

# Import the csv module to read csv files
import csv

def print_and_write(file_name,output):
	print(output)
	file_name.write(output+"\n")

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first
	csv_header = next(csvreader)

	# Initialize several variables
	total_number_of_months=1
	net_total_amount=0
	
	greatest_inc=0
	greatest_dec=0
	
	# Read first line of numerical data to compute the first change in
	# Profits/Losses
	csv_first_row=next(csvreader)
	prev_profit_or_loss=int(csv_first_row[1])
	net_total_amount+=prev_profit_or_loss
	# net change will be last month profit/loss minus first month.
	net_change=-prev_profit_or_loss

	for row in csvreader:
		total_number_of_months+=1
		# Get current months Profit/Loss
		cur_profit_or_loss=int(row[1])
		# Store diffrence in Profit/Loss
		row_profit_or_loss_change=cur_profit_or_loss-prev_profit_or_loss
		# Summ the net amount
		net_total_amount+=cur_profit_or_loss

		# Check if current month's change is greater or less than all
		# previous months' changes. 
		if greatest_inc< row_profit_or_loss_change:
			greatest_inc =row_profit_or_loss_change
			greatest_inc_mnth = row[0]
		elif greatest_dec > row_profit_or_loss_change:
			greatest_dec = row_profit_or_loss_change
			greatest_dec_mnth = row[0]
		# Store the current Profit/Loss as the previous one for the next
		# row.
		prev_profit_or_loss=cur_profit_or_loss
net_change+=cur_profit_or_loss
# Set up file for writing
output_file=open("results.txt", "w")
# Print all outputs
print("")
print_and_write(output_file,"Financial Analysis \n ----------------------------")
print_and_write(output_file,f"Total Months: {total_number_of_months}")
print_and_write(output_file,f"Total: ${net_total_amount:,}")
print_and_write(output_file,f"Average Change:  {round(1.0*net_change/(total_number_of_months-1),2):,}")
print_and_write(output_file,f"Greatest Increase in Profits:  "+greatest_inc_mnth+f" (${greatest_inc:,})")
print_and_write(output_file,f"Greatest Decrease in Profits:  "+greatest_dec_mnth+f" (${greatest_dec:,})\n")
output_file.close()