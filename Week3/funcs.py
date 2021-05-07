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

        if (choice != 'All'):
             if(key == choice):
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

def category_totals(data, choice):
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
        if(choice != 'All'):
            if(vendor_dict[vendor] == choice):
                print(key, value)
        else:
            print(key, value)
