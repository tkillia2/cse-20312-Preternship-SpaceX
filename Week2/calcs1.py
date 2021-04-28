#!/usr/bin/env python3

# Goal of this program is to further understanding of Python's Data Structures
# as well as practice calculating an average value for each category for each company

import csv
from collections import defaultdict


# Following Lines are from previous work to parse and input file, as well as read data into structure (uses lists and dictionaries
# See Dictionary.py in Week1 for more explanation of the lines until line 39
csv_file = open('SpaceXData.txt')

csv_file = csv_file.readlines()[1:]

csv_reader = csv.reader(csv_file, delimiter = ',')          

company_dict = defaultdict(list)                # Make a default dictionary and have it be made for lists (touched on in Bui's Class)


for row in csv_reader:
	key = row[0]                # Make the dictionary Key the first element of the newly seperated rows so that it is the company name
	row[5] = row[5].rstrip('%')  # Remove the percent sign from the last row of data
	value = row[1:]          # Have the value become a list of the following row elements ie excel sheet columns


	company_dict[key].append(row[1:]) # Add the list of elements to the value section for the given key


## USED TO PRINT 
# Formatted so that the Key is printed above followed by a new line for each Value before the new Key is Wrote
#for key, value in company_dict.items():
    #print('\n---------------NEW VENDOR INFO---------------\n')                # Line is written for when all data is displayed to make it easier to find new data
    #print('KEY: {}'.format(key))
    #for item in value:
        #print("\tValues: {}".format(item))  


print("\n--COMPANY-----QUALITY------COST------DELIVERY-----\n")			# Line for formatting of data

for value in company_dict.items():			# Iterates through each company, resetting the variables each time
	total_delivery = 0
	total_cost = 0
	total_quality = 0
	count = 0

	for list in value[1]:							# Iterates through the individual lists of value for each company
		total_delivery += int(list[0])  		# Sums up days past PO
		total_cost += int(list[4])		# Sums up cost % from target
		total_quality += (int(list[2]) + int(list[3])) / int(list[1])		# Adds nonconforming units and units that failed downstream, divides by lot size
		count += 1			# Increments count to be used later to calculate averages

	print(f"     {value[0]} {total_quality/count:14.4} {total_cost/count:9.4} {total_delivery/count:11.4}\n") 		# Prints averages of each category for current company with formatting
