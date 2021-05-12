#!/usr/bin/env python3

import csv
from collections import defaultdict
from collections import OrderedDict

# raw_vendor
# Function executes the same code as Dictionary.py
# Please refer to original file for more in depth explanation
# Function arguments: data file (string), vendor(string)
# Function returns a dictionary for a single vendor
# Vendor is determined by the command line argument after flag for this function (-r)
# Vendor could also be all vendors
# For example './main.py -r SpaceXData A'
# Example for all './main.py -r SpaceXData All'
def raw_vendor(data, choice):

    csv_file    = open(data) # open the data file

    csv_file    = csv_file.readlines()[1:] # read in line by line

    csv_reader  = csv.reader(csv_file, delimiter = ',')

    vendor_dict = defaultdict(list) # create empty dictionary ready for lists


    # Fill in the dictionary with corresponding vendor data
    for row in csv_reader:
        key   = row[0]
        value = row[1:]

        if choice != 'All':
             if key == choice:
                vendor_dict[key].append(row[1:])
        else:
            vendor_dict[key].append(row[1:])

    return  vendor_dict



# print_vendor_data
# Function executes the last portion of Dictionary.py
# Format is that of header, then vendor, then raw data values
# Created seperate in order to allow for either a single vendor to be printed or for all to be printed
# Function arguments: vendor_dict(dictionary created by above functions)
# function return value: none, prints to terminal
def print_vendor_data(vendor_dict):

    for key, value in vendor_dict.items():

        print(f'\n---------------VENDOR {key} INFO---------------\n')
        print('KEY: {}'.format(key))
        print('VALUES:')
        for item in value:
             print("\t {}".format(item))
        print('\n')



# category_totals
# Function executes the creation of dictionary seen in fileDict.py
# The purpose is to read in the data and total each category for each vendor
# For greater detail see original file
# This function also displays the totals to the terminal
# Use can specify a vendor or choose all, like with the raw data
# flag is -t
# Single vendor example './main.py -t SpaceXData A'
# All vendor example './main.py -t SpaceXData All'

def category_totals(data):

    csv_file    = open(data)
    csv_file    = csv_file.readlines()[1:]
    vendor_dict = defaultdict(dict)

    for row in csv_file:
        vendor, daysPastPO, lotSize, nonconUnits, failedUnits, cost = row.split(',')
        cost = cost.rstrip('%\n')

        vendor_dict[vendor]['daysPastPO']  = vendor_dict[vendor].get('daysPastPO', 0) + int(daysPastPO)
        vendor_dict[vendor]['lotSize']     = vendor_dict[vendor].get('lotSize', 0) + int(lotSize)
        vendor_dict[vendor]['nonconUnits'] = vendor_dict[vendor].get('nonconUnits', 0) + int(nonconUnits)
        vendor_dict[vendor]['failedUnits'] = vendor_dict[vendor].get('failedUnits', 0) + int(failedUnits)
        vendor_dict[vendor]['cost']        = vendor_dict[vendor].get('cost', 0) + int(cost)

    for key, value in vendor_dict.items():
        print(key, value)

# vendor_averages
# Function executes the display of data averages for each category seen in calcOrder.py
# The purpose is to print out an average value for delivery, cost, and quality per company
# Only prints the first table
# Flag is -a (no need to specify vendor
# Example run './main.py -a SpaceXData'

def vendor_averages(data):

    csv_file    = open(data)
    csv_file    = csv_file.readlines()[1:]
    csv_reader  = csv.reader(csv_file, delimiter = ',')
    vendor_dict = defaultdict(list)
    List = []

    for row in csv_reader:
        key    = row[0]
        row[5] = row[5].rstrip('%')
        value  = row[1:]
            
        vendor_dict[key].append(row[1:])

        
    print('\n---VENDOR------QUALITY------COST------DELIVERY----')
    for value in vendor_dict.items():
        total_delivery = 0
        total_cost     = 0
        total_quality  = 0
        count          = 0

        for List in value[1]:
            total_delivery += int(List[0])
            total_cost     += int(List[4])
            total_quality  += (int(List[2]) + int(List[3])) / int(List[1])
            count          += 1
        print(f'     {value[0]} {(1-(total_quality/count))*100:14.4}% {total_cost/count:9.4}% {total_delivery/count:11.4}\n')


# vendor_grades
# Function executes the display of data averages for each category seen in calcOrder.py
# The purpose is to print out an average value for delivery, cost, and quality per company as well as the score and decision
# Only prints the second table
# Flag is -g (no need to specify vendor)
# Example run './main.py -g SpaceXData'

def vendor_grades(data):

    csv_file    = open(data)
    csv_file    = csv_file.readlines()[1:]
    csv_reader  = csv.reader(csv_file, delimiter = ',')
    vendor_dict = defaultdict(list)
    List = []

    for row in csv_reader:
        key    = row[0]
        row[5] = row[5].rstrip('%')
        value  = row[1:]
            
        vendor_dict[key].append(row[1:])

    print("\n--COMPANY-----QUALITY------COST------DELIVERY------SCORE--\n")

    GPA = []

    for value in vendor_dict.items():
        total_delivery = 0
        total_cost = 0
        total_quality = 0
        count = 0
        GPA_start = 4.00
        GPA_test = 4.00
        decision = 'GROW'

        for List in value[1]:
            total_delivery += int(List[0])
            total_cost += int(List[4])
            total_quality += (int(List[2]) + int(List[3])) / int(List[1])
            count += 1

        qualScore = total_quality/count * 100
        costScore = total_cost/count * 0.1
        delivScore = total_delivery/count * 0.1

        GPA_test = GPA_test - 0.12*qualScore - 0.04*costScore - 0.08*delivScore
        print(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {costScore*10:9.4}% {delivScore*10:11.4}   | {GPA_test:8.4}\n")
        
        '''
        GPA.append(GPA_start - 0.12*qualScore - 0.04*costScore - 0.08*delivScore)


      #  if GPA < 3.55 and GPA > 3.45:
         #   decision = 'MAINTAIN'
       # elif GPA <= 3.45:
           # decision = 'EXIT'

    grade_dict = {}
    ascii = 65
    for element in GPA:
        key = chr(ascii)
        grade_dict[key] = element
        ascii += 1

    grade_dict = sorted(grade_dict.items(), key = lambda x: x[1], reverse = True)
    GPA = sorted(GPA, reverse = True)

    iter = 0
    for value in grade_dict:
        decision = "GROW"
        key = grade_dict[iter][0]
        if iter < 7 and iter > 3:
            decision = "MAINTAIN"
        elif iter > 6:
            decision = "EXIT"
        if key == 'F':
            decision += '**'
        print(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {costScore*10:9.4}% {delivScore*10:11.4}   | {GPA[iter]:8.4}   -> {decision:10}")
        print("                                                |")
        iter += 1
'''

# score_vendors
# Function calculates the overall score for each company as seen in calcOrder2.py
# The purpose is to print out each company's score and decision in a row by row format
# flag is -s 
# Example run './main.py -s SpaceXData'

def score_vendors(data):
    csv_file    = open(data)
    csv_file    = csv_file.readlines()[1:]
    csv_reader  = csv.reader(csv_file, delimiter = ',')
    vendor_dict = defaultdict(list)
    List = []

    for row in csv_reader:
        key    = row[0]
        row[5] = row[5].rstrip('%')
        value  = row[1:]

        vendor_dict[key].append(row[1:])

    for value in vendor_dict.items():
        total_delivery = 0
        total_cost     = 0
        total_quality  = 0
        count          = 0

        for List in value[1]:
            total_delivery += int(List[0])
            total_cost     += int(List[4])
            total_quality  += (int(List[2]) + int(List[3])) / int(List[1])
            count          += 1
        
    GPA = []

    for value in vendor_dict.items():
        total_delivery = 0
        total_cost = 0
        total_quality = 0
        count = 0
        Gpa_test = 4.00
        Gpa_start = 4.00
        decision = "GROW"

        for list0 in value[1]:
            total_delivery += int(list0[0])
            total_cost += int(list0[4])
            total_quality += (int(list0[2]) + int(list0[3])) / int(list0[1])
            count += 1

        qualScore = total_quality/count * 100
        costScore = total_cost/count * 0.1
        delivScore = total_delivery/count * 0.1
        Gpa_test = Gpa_test - 0.12*qualScore - 0.04*costScore - 0.08*delivScore

        GPA.append(Gpa_start - 0.12*qualScore - 0.04*costScore - 0.08*delivScore)

    grade_dict = {}
    ascii = 65
    for element in GPA:
        key = chr(ascii)
        grade_dict[key] = element
        ascii += 1

    vendor_f = False;
    grade_dict = sorted(grade_dict.items(), key = lambda x: x[1], reverse = True)
    iter = 0
    for value in grade_dict:
        status = "GROW"
        key = grade_dict[iter][0]
        if iter < 7 and iter > 3:
            status = "MAINTAIN"
        elif iter > 6:
            status = "EXIT"
        if key == 'F':
            status += '**'
            vendor_f = True;

        if iter == 0:
            print()
        
        print(f"Vendor: {grade_dict[iter][0]}    Score: {grade_dict[iter][1]:.4}    Decision: {status}\n\n")
        iter += 1
    if (vendor_f) :
        print("**Due to limited information from Vendor F, they will receive GROW status.\n")
        print("However, in order to provide the best results we have decided that vendor F has too little information compared to the others.\n")
        print("Therefore we have expanded the grow category to four vendors, with this footnote for F.\n")


# grade_to_Out
# Function creates grading and scoring table 
# Creates text file that will be written to with the tables created
# Flag -o
# Example './main.py -o SpaceXData

def grade_to_Out(data):
    csv_file = open('SpaceXData.txt')
    
    outFile = open('Outfile.txt', 'w')
    
    csv_file = csv_file.readlines()[1:]

    csv_reader = csv.reader(csv_file, delimiter = ',')

    vendor_dict = defaultdict(list)

    for row in csv_reader:
        key    = row[0]
        row[5] = row[5].rstrip('%')
        value  = row[1:]

        vendor_dict[key].append(row[1:])

    outFile.write("\n--COMPANY-----QUALITY------COST------DELIVERY------SCORE--\n\n")

    GPA = []

    for value in vendor_dict.items():
        total_delivery  = 0
        total_cost      = 0
        total_quality   = 0
        count           = 0
        GPA_start       = 4.00
        GPA_test        = 4.00
        decision        = 'GROW' 
    
        for List in value[1]:
            total_delivery += int(List[0])
            total_cost += int(List[4])
            total_quality += (int(List[2]) + int(List[3])) / int(List[1])
            count += 1

        qualScore = total_quality/count * 100
        costScore = total_cost/count * 0.1
        delivScore = total_delivery/count * 0.1
        GPA_test = GPA_test - 0.12*qualScore - 0.04*costScore - 0.08*delivScore

        outFile.write(f"     {value[0]} {(1-(total_quality/count))*100:14.4}% {costScore*10:9.4}% {delivScore*10:11.4}   | {GPA_test:8.4}\n")
        outFile.write("                                                |\n")
        outFile.write('\n')

        GPA.append(GPA_start - 0.12*qualScore - 0.04*costScore - 0.08*delivScore)

    grade_dict = {}
    ascii = 65
    
    for element in GPA:
        key = chr(ascii)
        grade_dict[key] = element
        ascii += 1

    grade_dict = sorted(grade_dict.items(), key = lambda x: x[1], reverse = True)
    iter = 0

    for value in grade_dict:
        status = "GROW"
        key = grade_dict[iter][0]
        if iter < 7 and iter > 3:
            status = "MAINTAIN"
        elif iter > 6:
            status = "EXIT"
        if key == 'F':
            status += '**'

        outFile.write(f"Vendor: {grade_dict[iter][0]}    Score: {grade_dict[iter][1]:.4}    Decision: {status}\n\n")
        iter += 1

    outFile.write("**Due to limited information from Vendor F, they will receive GROW status.\n")
    outFile.write("However, in order to provide the best results we have decided that vendor F has too little information compared to the others.\n")
    outFile.write("Therefore we have expanded the grow category to four vendors, with this footnote for F.\n")
