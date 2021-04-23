#!/usr/bin/env python3

## Goal of this program is to boost understanding of utilizing Python's Data Structures
# Predominantly Dictionaries -- Hoping to create a dictionary with Company Name as the Key
# And then having the other columns from the Excel Sheet be the values

import csv
from collections import defaultdict


# Following Lines are from previous work to parse and input file
csv_file = open('SpaceXData.txt')

# remove top line with strings that describe the info ie Days Past PO etc. this way all numbers and key
csv_file = csv_file.readlines()[1:]

csv_reader = csv.reader(csv_file, delimiter = ',')          

company_dict = defaultdict(list)                # Make a default dictionary and have it be made for lists (touched on in Bui's Class)


for row in csv_reader:
    key = row[0]                # Make the dictionary Key the first element of the newly seperated rows so that it is the company name
    value = row[1:]             # Have the value become a list of the following row elements ie excel sheet columns

    ## To print all Keys and Values and have it appear like the spreadsheet just comment out if statement and remove tab before following line
    if(key == 'A'):                             # Line is done for smaller appearence -- values match with Excel Sheet Key and Values Split
        company_dict[key].append(row[1:])           # Add the list of elements to the value section for the given key


## USED TO PRINT 
# Formatted so that the Key is printed above followed by a new line for each Value before the new Key is Wrote
for key, value in company_dict.items():
    print('\n---------------NEW VENDOR INFO---------------\n')                # Line is written for when all data is displayed to make it easier to find new data
    print('KEY: {}'.format(key))
    for item in value:
        print("\tValues: {}".format(item))  


