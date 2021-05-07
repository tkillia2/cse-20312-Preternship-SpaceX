#!/usr/bin/env python3

import xlwt
from xlwt import Workbook

import csv
from collections import defaultdict


# Following Lines are from previous work to parse and input file, as well as read data into structure (uses lists and dictionaries
# See Dictionary.py in Week1 for more explanation of the lines until line 39

wb = Workbook()

sheet1 = wb.add_sheet('Data Output')

csv_file = open('SpaceXData.txt')

csv_file = csv_file.readlines()[1:]

csv_reader = csv.reader(csv_file, delimiter = ',')          

company_dict = defaultdict(list)                # Make a default dictionary and have it be made for lists (touched on in Bui's Class)


for row in csv_reader:
	key = row[0]                # Make the dictionary Key the first element of the newly seperated rows so that it is the company name
	row[5] = row[5].rstrip('%')  # Remove the percent sign from the last row of data
	value = row[1:]          # Have the value become a list of the following row elements ie excel sheet columns


	company_dict[key].append(row[1:])
'''
outFile.write("\n--COMPANY-----QUALITY------COST------DELIVERY-----\n\n")
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
	outFile.write(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {total_cost/count:9.4}% {total_delivery/count:11.4}\n\n") 		# Prints averages of each category for current company with formatting
'''





sheet1.write(0, 0, 'COMPANY')
sheet1.write(1, 0, 'QUALITY')
sheet1.write(2, 0, 'COST')
sheet1.write(3, 0, 'DELIVERY')
sheet1.write(4, 0, 'SCORE')

GPA = []

row = 1

for value in company_dict.items():			# Iterates through each company, resetting the variables each time
    total_delivery = 0
    total_cost = 0
    total_quality = 0
    count = 0
    GPA_start = 4.00          # Creating GPA and decision variables
    Gpa_test = 4.00
    decision = "GROW"

    for list in value[1]:							# Iterates through the individual lists of value for each company
	    total_delivery += int(list[0])  		# Sums up days past PO
	    total_cost += int(list[4])		# Sums up cost % from target
	    total_quality += (int(list[2]) + int(list[3])) / int(list[1])		# Adds nonconforming units and units that failed downstream, divides by lot size
	    count += 1			# Increments count to be used later to calculate averages

    qualScore = total_quality/count * 100
    costScore = total_cost/count * 0.1
    delivScore = total_delivery/count * 0.1
    Gpa_test = Gpa_test - 0.12*qualScore - 0.04*costScore - 0.08*delivScore

  #  outFile.write(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {costScore*10:9.4}% {delivScore*10:11.4}   | {Gpa_test:8.4}\n")
    sheet1.write(0, row, value[0]) 
    sheet1.write(1, row, (1-(total_quality/count))*100)
    sheet1.write(2, row, costScore*10)
    sheet1.write(3, row, delivScore*10)
    sheet1.write(4, row, Gpa_test)

    row += 1


    GPA.append(GPA_start - 0.12*qualScore - 0.04*costScore - 0.08*delivScore) # Calculating GPA using formula

grade_dict = {}
ascii = 65
for element in GPA:
    key = chr(ascii)
    grade_dict[key] = element
    ascii += 1

grade_dict = sorted(grade_dict.items(), key = lambda x: x[1], reverse = True)
iter = 0
row = 14
sheet1.write(0, 13, 'VENDOR') 
sheet1.write(1, 13, 'SCORE') 
sheet1.write(2, 13, 'DECISION')
 
for value in grade_dict:
    status = "GROW"
    key = grade_dict[iter][0]
    if iter < 7 and iter > 3:
        status = "MAINTAIN"
    elif iter > 6:
        status = "EXIT"
    if key == 'F':
        status += '**'
    
 #   print(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {costScore*10:9.4}% {delivScore*10:11.4}   | {GPA:8.4}   -> {decision:10}")
  #  print("                                                |")			    # Prints averages of each category for current company with formatting
    sheet1.write(0, row, grade_dict[iter][0]) 
    sheet1.write(1, row, grade_dict[iter][1]) 
    sheet1.write(2, row, status) 
   # outFile.write(f"Vendor: {grade_dict[iter][0]}    Score: {grade_dict[iter][1]:.4}    Decision: {status}\n\n")
    iter += 1
    row += 1

# outFile.write("**Due to limited information from Vendor F, they will receive GROW status.\n")
# outFile.write("However, in order to provide the best results we have decided that vendor F has too little information compared to the others.\n")
 #outFile.write("Therefore we have expanded the grow category to four vendors, with this footnote for F.\n")

sheet1.write(0, 28, '**Due to limited information from Vendor F, they will receive GROW status.  However, in order to provide the best results we have decided that vendor F has too little information compared to the others.  Therefore we have expanded the grow category to four vendors, with this footnote for F."')

wb.save('DataOutput.xls')
