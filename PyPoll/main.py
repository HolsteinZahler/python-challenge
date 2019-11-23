# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

def print_and_write(file_name,output):
	print(output)
	file_name.write(output+"\n")

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	#print(csvreader)

	# Read the header row first (skip this step if there is now header)
	csv_header = next(csvreader)
	
	Election_Results={}
	row_number=0
	for row in csvreader:
		row_number+=1
#		if row_number < 5:
#			print(row)
		if row[2] in Election_Results:
			Election_Results[row[2]]+=1
		else:
			Election_Results[row[2]]=1
winner_total=0
output_file=open("results.txt", "w")
print("")
print_and_write(output_file,"Election Results")
print_and_write(output_file,"-------------------------")
print_and_write(output_file,f"Total Votes: {row_number}")
print_and_write(output_file,"-------------------------")
for x in Election_Results:
	print_and_write(output_file,x+f": {round(100.0*Election_Results[x]/row_number,3):0.3f}% ({Election_Results[x]}) votes.")
	if Election_Results[x]>winner_total:
		winner=x
		winner_total=Election_Results[x]
print_and_write(output_file,"-------------------------")
print_and_write(output_file,winner)
print_and_write(output_file,"-------------------------")
print("")
