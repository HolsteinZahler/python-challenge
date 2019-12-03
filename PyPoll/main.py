# Import the os module to create file paths across operating systems
import os

# Import the csv module to read csv files
import csv

# Function to print a string to file and to the screen.
def print_and_write(file_name,output):
	print(output)
	file_name.write(output+"\n")

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	# Read the header row first (skip this step if there is now header)
	csv_header = next(csvreader)
	
	Election_Results={}
	Detailed_Election_Results={}
	row_number=0
	for row in csvreader:
		row_number+=1
		# Checks if the candidate is already in the dictionary.  If they
		# are, one is added to their vote tally.  Otherwise, the 
		# candidate's name is added to the dictionary and their vote 
		# tally is initialized.
		if row[2] in Election_Results:
			Election_Results[row[2]]+=1
		else:
			Election_Results[row[2]]=1
		# This outer if statement checks if a county is in the 
		# Detailed_Election_Results dictionary and adds the county if it
		# is missing.  
		# The nested if statement is similar to the previous if 
		# statement.  
		if row[1] in Detailed_Election_Results:
			if row[2] in Detailed_Election_Results[row[1]]:
				Detailed_Election_Results[row[1]][row[2]]+=1
			else:
				Detailed_Election_Results[row[1]][row[2]]=1
		else:
			Detailed_Election_Results[row[1]]={}
			Detailed_Election_Results[row[1]][row[2]]=1

# Initializes a place to store the number of votes 
# the winning candidate receives.
winner_total=0
# Prints the first few rows of output.
output_file=open("results.txt", "w")
print("")
print_and_write(output_file,"Election Results")
print_and_write(output_file,"-------------------------")
print_and_write(output_file,f"Total Votes: {row_number}")
print_and_write(output_file,"-------------------------")
# Cycles through candidates names, prints their vote percentage and 
# tally.  
for x in Election_Results:
	print_and_write(output_file,x+f": {round(100.0*Election_Results[x]/row_number,3):0.3f}% ({Election_Results[x]}) votes.")
	if Election_Results[x]>winner_total:
		winner=x
		winner_total=Election_Results[x]
# Prints the name of the candidate that received the most votes.
print_and_write(output_file,"-------------------------")
print_and_write(output_file,winner)
print_and_write(output_file,"-------------------------")
print("")

#The remaining code is for County-by-county Election Results.

# Creates lists of candidates and counties
candidate_list=[]
county_list=[]
for x in Detailed_Election_Results:
	if x not in county_list:
		county_list.append(x)
	for y in Detailed_Election_Results[x]:
		if y not in candidate_list:
			candidate_list.append(y)

# Alphabatize candidate and county names
candidate_list.sort()
county_list.sort()


max_char_lengths=[0]
#Initialize widths of collumns using names and width needed for 
# percentages.
for x in candidate_list:
	max_char_lengths.append(max(len(x),8))

county_total=[]
#Loop to get maximum widths of strings for table and votes cast 
# in each county
for x in county_list:
	temp_string=x
	county_vote_sum=0
	if len(temp_string)>max_char_lengths[0]:
		max_char_lengths[0]=len(temp_string)
	count=0
	for name in candidate_list:
		count+=1
		if name in Detailed_Election_Results[x]:
			max_char_lengths[count]=max( len(str(Detailed_Election_Results[x][name]))+2, max_char_lengths[count] )
			county_vote_sum+=Detailed_Election_Results[x][name]
	county_total.append(county_vote_sum)

#Allow for one space to be added on both sides of longest table entry
max_char_lengths=[x+2 for x in max_char_lengths]
#Get length of each output string adding | left of each entry and an 
# extra one for the right side of the column.
output_width=len(max_char_lengths)+sum(max_char_lengths)+1
#Print the title for the output table
print_and_write(output_file,"")
print_and_write(output_file,"County-by-county Election Results")
print_and_write(output_file,"-"*output_width)
#Creates the first row of the table that contains the candidate names 
# and border underneath.
row_string=" "+" ".center(max_char_lengths[0])
count=0
for j in candidate_list:
	count+=1
	row_string+="|"+j.center(max_char_lengths[count])
print_and_write(output_file,row_string+"|")
print_and_write(output_file,"-"*output_width)
#Creates remaining rows of table with borders underneath
county_number=0
for x in county_list:
    count=0
    row_string="|"+" ".center(max_char_lengths[count])
    percent_row_string="|"+x.center(max_char_lengths[count])
    for name in candidate_list:
        count+=1
        if name in Detailed_Election_Results[x]:
            row_string+="|"+("("+str(Detailed_Election_Results[x][name])+")").center(max_char_lengths[count])
            percent_row_string+="|"+f"{round(100.0*Detailed_Election_Results[x][name]/county_total[county_number],3):0.3f}%".center(max_char_lengths[count])
        else:  #Handles case where candidate gets no votes in a county
            row_string=row_string+"|"+str(0).center(max_char_lengths[count])
            percent_row_string+=f": {round(0,3):0.3f}%"
    print_and_write(output_file,percent_row_string+"|")
    print_and_write(output_file,row_string+"|")
    print_and_write(output_file,"-"*output_width)
    county_number+=1

