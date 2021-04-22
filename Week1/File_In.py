#!/usr/bin/env python3

# SpaceX Preternship Team -- Week 1 Determine how to read in the dummy data and parse through it


import csv      # Data is stored in a comma seperated file, library will be used to parse through the data

# Open the SpaceX Dummy Data File
#f = open("SpaceXData.txt", "r")

# Prints this data out just as it is in the file to prove the file has been accessed
# print(f.read());


## NOW TAKE DATA IN AS CSV
csv_file =  open('SpaceXData.txt')

# Removes the first row in the file which consists of Titles for each column (done if necessary)
csv_file = csv_file.readlines()[1:]

# Works through the file to seperate elements by commas
csv_reader = csv.reader(csv_file, delimiter = ',')

##### CREATION OF VARIABLES IN ORDER TO TEST UNDERSTANDING OF DIFFERENT ELEMENTS WITHIN THE PARSED DATA
# OPERATIONS ARE PERFORMED BELOW WITHIN THE FOR LOOP -- USED AS TESTS

LateDaysA = 0

# Add Together Nonconforming units and units that failed downstream for Vendor B
BadUnitsB = 0
LateBadUnitsB = 0
# Divide that by total of lot size to get percent of total failed units
LotSizeB = 0

# Works through the rows of the file
for row in csv_reader:
    #print(row)          # Prints data out as rows with individual elements ie ['J','9','277','9','5','49%']

    # Attempt to remove the percent sign at the end of the last element ie 49% above just becomes 49
    if row[5].endswith('%'):
        row[5] = row[5].rstrip('%')
        #print(row[5])      check to see if this works and it does, percent symbol is no longer on the end of the final element
    
    #print(row)          # data now appears as ['J','9','277','9','5','49'] -- no more percent symbol

    # Use this to total up the number of late days for all vendors changing A to whatever other letter is used to reference the vendor
    if(row[0] == 'A'):
        LateDaysA += int(row[1])        # typecast to int

    if(row[0] == 'B'):
        BadUnitsB += float(row[3])          # typecast to float for defective unit variables in order to perform correct division
        LateBadUnitsB += float(row[4])
        LotSizeB += float(row[2])

    print(row)

# Prints 627 -- which is correct when checking with the provided Excel sheet --  that is the total number of Days past PO for company A
print(LateDaysA)

# Prints number as a decimal should convert to percentage -- however correctly done when checked with Excel sheet
print( ( BadUnitsB+LateBadUnitsB )/LotSizeB )

