#!/usr/bin/env python3

import csv
import sys
from collections import defaultdict
from collections import OrderedDict
from funcs import raw_vendor # import from funcs.py  
from funcs import print_vendor_data # import from funcs.py
from funcs import category_totals

def main():
    arguments = sys.argv[1:] # store command line arguments not inluding file name
    # iterate through command line arguments
    while arguments:
        # take first command line argument
        argument = arguments.pop(0)
        if argument == '-r': # raw vendor flag (one or all)
            argument = arguments.pop(0) # pop again to get data file
            vendor = arguments.pop(0) # since we need the vendor as well we pop again to get next argument as vendor
            vendor_dict = raw_vendor(argument, vendor) # create dictionary for specified vendor raw data
            print_vendor_data(vendor_dict) # print data
        elif argument == '-t':
            argument = arguments.pop(0)
            category_totals(argument)
             
if __name__ == '__main__':
    main()
