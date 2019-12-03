# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

def print_and_write(file_name,output):
	print(output)
	file_name.write(output+"\n")

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	#print(csvreader)

	# Read the header row first (skip this step if there is now header)
	csv_header = next(csvreader)
	total_number_of_months=0
	net_total_amount=0
	net_change=0

	greatest_inc=0
	greatest_dec=0
	
	total_number_of_months=1
	csv_first_row=next(csvreader)
	prev_profit_or_loss=int(csv_first_row[1])
	net_total_amount+=prev_profit_or_loss
	
	for row in csvreader:
		total_number_of_months+=1
		cur_profit_or_loss=int(row[1])
		row_profit_or_loss_change=cur_profit_or_loss-prev_profit_or_loss
		net_total_amount+=cur_profit_or_loss
		net_change+=row_profit_or_loss_change
#		if total_number_of_months < 5:
#			print(row)
		if greatest_inc< row_profit_or_loss_change:
			greatest_inc =row_profit_or_loss_change
			greatest_inc_mnth = row[0]
		elif greatest_dec > row_profit_or_loss_change:
			greatest_dec = row_profit_or_loss_change
			greatest_dec_mnth = row[0]
		prev_profit_or_loss=int(row[1])
output_file=open("results.txt", "w")
print("")
print_and_write(output_file,"Financial Analysis \n ----------------------------")
print_and_write(output_file,f"Total Months: {total_number_of_months}")
print_and_write(output_file,f"Total: ${net_total_amount:,}")
print_and_write(output_file,f"Average Change:  {round(1.0*net_change/(total_number_of_months-1),2):,}")
print_and_write(output_file,f"Greatest Increase in Profits:  "+greatest_inc_mnth+f" (${greatest_inc:,})")
print_and_write(output_file,f"Greatest Decrease in Profits:  "+greatest_dec_mnth+f" (${greatest_dec:,})\n")
output_file.close()
#print(1.0*net_total_amount/total_number_of_months)
#print(greatest_inc)
#print(greatest_dec)
