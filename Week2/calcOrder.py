#!/usr/bin/env python3

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


	company_dict[key].append(row[1:])

print("\n--COMPANY-----QUALITY------COST------DELIVERY-----\n")

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

	print(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {total_cost/count:9.4}% {total_delivery/count:11.4}\n") 		# Prints averages of each category for current company with formatting






print("\n--COMPANY-----QUALITY------COST------DELIVERY------SCORE------DECISION--\n")

GPA = []

for value in company_dict.items():			# Iterates through each company, resetting the variables each time
	total_delivery = 0
	total_cost = 0
	total_quality = 0
	count = 0
	GPA = 4.00          # Creating GPA and decision variables
	decision = "GROW"

	for list in value[1]:							# Iterates through the individual lists of value for each company
		total_delivery += int(list[0])  		# Sums up days past PO
		total_cost += int(list[4])		# Sums up cost % from target
		total_quality += (int(list[2]) + int(list[3])) / int(list[1])		# Adds nonconforming units and units that failed downstream, divides by lot size
		count += 1			# Increments count to be used later to calculate averages

	qualScore = total_quality/count * 100
	costScore = total_cost/count * 0.1
	delivScore = total_delivery/count * 0.1

	GPA = GPA - 0.04*qualScore - 0.03*costScore - 0.03*delivScore # Calculating GPA using formula

	if GPA < 3.55 and GPA > 3.45: # Judging based on the GPA whether to GROW, MAINTAIN, or EXIT
		decision = "MAINTAIN"
	elif GPA <= 3.45:
		decision = "EXIT"

	print(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {costScore*10:9.4}% {delivScore*10:11.4}   | {GPA:8.4}   -> {decision:10}")
	print("                                                |")																						# Prints averages of each category for current company with formatting







