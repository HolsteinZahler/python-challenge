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
	Detailed_Election_Results={}
	row_number=0
	for row in csvreader:
		row_number+=1
#		if row_number < 5:
#			print(row)
		if row[2] in Election_Results:
			Election_Results[row[2]]+=1
		else:
			Election_Results[row[2]]=1
		if row[1] in Detailed_Election_Results:
			if row[2] in Detailed_Election_Results[row[1]]:
				Detailed_Election_Results[row[1]][row[2]]+=1
			else:
				Detailed_Election_Results[row[1]][row[2]]=1
		else:
			Detailed_Election_Results[row[1]]={}
			Detailed_Election_Results[row[1]][row[2]]=1


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

candidate_list=[]
county_list=[]
for x in Detailed_Election_Results:
	if x not in county_list:
		county_list.append(x)
	for y in Detailed_Election_Results[x]:
		if y not in candidate_list:
			candidate_list.append(y)

candidate_list.sort()
county_list.sort()
#print(candidate_list)
#print(county_list)

print_and_write(output_file,"")
print_and_write(output_file,"Detailed Election Results")
print_and_write(output_file,"-------------------------")
max_char_lengths=[0]
for x in candidate_list:
	max_char_lengths.append(len(x))

#print(max_char_lengths)
for x in county_list:
	my_string=x
	if len(my_string)>max_char_lengths[0]:
		max_char_lengths[0]=len(my_string)
	count=0
	for name in candidate_list:
		count+=1
		if name in Detailed_Election_Results[x]:
			if len(str(Detailed_Election_Results[x][name]))>max_char_lengths[count]:
				max_char_lengths[count]=len(str(Detailed_Election_Results[x][name]))
			my_string=my_string+" "+str(Detailed_Election_Results[x][name])
		else:
			my_string=my_string+" "+str(0)

#print(my_string)

#print(max_char_lengths)

max_char_lengths=[x+2 for x in max_char_lengths]
output_width=len(max_char_lengths)+sum(max_char_lengths)+1

my_string=" "+" ".center(max_char_lengths[0])
count=0
for j in candidate_list:
	count+=1
	my_string+="|"+j.center(max_char_lengths[count])
print(my_string+"|")
print("-"*output_width)
for x in county_list:
	count=0
	my_string="|"+x.center(max_char_lengths[count])
	for name in candidate_list:
		count+=1
		if name in Detailed_Election_Results[x]:
			my_string=my_string+"|"+str(Detailed_Election_Results[x][name]).center(max_char_lengths[count])
		else:
			my_string=my_string+"|"+str(0).center(max_char_lengths[count])
	print(my_string+"|")
	print("-"*output_width)


#print(max_char_lengths)

#for x in Detailed_Election_Results:
#	print(x)
#	for y in Detailed_Election_Results[x]:
#		print(y + ": " +str(Detailed_Election_Results[x][y]))
#		print(Detailed_Election_Results[x][y])
#		out_string=y+str(Detailed_Election_Results[x][y])
