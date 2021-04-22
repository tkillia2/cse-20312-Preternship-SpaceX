#!/usr/bin/env python3

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

# Works through the rows of the file
for row in csv_reader:
    #print(row)          # Prints data out as rows with individual elements ie ['J','9','277','9','5','49%']

    # Attempt to remove the percent sign at the end of the last element ie 49% above just becomes 49
    if row[5].endswith('%'):
        row[5] = row[5].rstrip('%')
        #print(row[5])      check to see if this works and it does, percent symbol is no longer on the end of the final element
    
    print(row)          # data now appears as ['J','9','277','9','5','49'] -- no more percent symbol



