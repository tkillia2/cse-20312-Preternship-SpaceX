#!/usr/bin/env python3

import csv
from collections import defaultdict
from collections import OrderedDict

# single_vendor
# Function executes the same code as Dictionary.py 
# Please refer to original file for more in depth explanation
# Function arguments: data file (string), vendor(string)
# Function returns a dictionary for a single vendor
# Vendor is determined by the command line argument after flag for this function (tbd)
# For example './funcs.py -flag "A"'

def single_vendor(data, vendor)

    csv_file    = open(data) # open the data file
    
    csv_file    = csv_file.readlines()[1:] # read in line by line

    csv_reader  = csv.reader(csv_file, delimeter = ',') 

    vendor_dict = defaultdict(list) # create empty dictionary ready for lists


    # Fill in the dictionary with corresponding vendor data
    for row in csv_reader:
        key   = row[0]
        value = row[1:]
    
        if(key == vendor):
            vendor_dict[key].append(row[1:])


    return  vendor_dict

# all_vendors
# Function executes same as above except that the dictionary created is 
# filled with the data from all vendors
# return dictionary of vendors

def all_vendors(data, vendor)

    csv_file    = open(data) # open the data file
    
    csv_file    = csv_file.readlines()[1:] # read in line by line

    csv_reader  = csv.reader(csv_file, delimeter = ',') 

    vendor_dict = defaultdict(list) # create empty dictionary ready for lists


    # Fill in the dictionary with corresponding vendor data
    for row in csv_reader:
        key   = row[0]
        value = row[1:]

    return  vendor_dict

# print_vendor_data
# Function executes the last portion of Dictionary.py
# Format is that of header, then vendor, then raw data values 
# Created seperate in order to allow for either a single vendor to be printed or for all to be printed 
# Function arguments: vendor_dict(dictionary created by above functions)
# function return value: none, prints to terminal
def print_vendor_data(vendor_dict)
    
    for key, value in vendor_dict.items():

        print('\n---------------VENDOR INFO---------------\n')
        print('KEY: {}'.format(key))

        for item in value:
             print("\tValues: {}".format(item))

# Function
