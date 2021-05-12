#!/usr/bin/env python3

import csv
import sys
import os
from collections import defaultdict
from collections import OrderedDict
from funcs import raw_vendor # import from funcs.py
from funcs import print_vendor_data # import from funcs.py
from funcs import category_totals
from funcs import vendor_averages
from funcs import score_vendors
from funcs import vendor_grades 
from funcs import grade_to_Out

def usage(status):
    ''' Display usage message and exit with status. '''
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [flags] [vendor (if applicable)]
    -r      Prints raw data for any or all vendors. Specify vendor with letter A-J or All for all vendors
    -t      Prints each vendors category totals. No need to specify vendor
    -g      Calculates grades for each vendor and displays score, GPA and suggestion. No need to specify vendor
    -s      Prints vendor and suggestion only. Specify vendor with letter A-J or All for all vendors
    -o      Allows for the outputs of both the -g and -s flags to be viewed in a file named Outfile.txt
    -h      Help, print usage
By default, {progname} prints one of each type of line.''')
    sys.exit(status)

def main():
    arguments = sys.argv[1:] # store command line arguments not inluding file name
    # iterate through command line arguments
    if len(arguments) < 2:
        usage(1)

    while arguments:
        # take first command line argument
        argument = arguments.pop(0)
        if argument == '-r': # raw vendor flag (one or all)
            argument = arguments.pop(0) # pop again to get data file
            vendor = arguments.pop(0) # since we need the vendor as well we pop again to get next argument as vendor
            vendor_dict = raw_vendor(argument, vendor) # create dictionary for specified vendor raw data
            print_vendor_data(vendor_dict) # print data
        elif argument == '-t': #category totals flag
            argument = arguments.pop(0)
            category_totals(argument)
        elif argument == '-a': # averages data flag
            argument = arguments.pop(0) # pop again to get data file
            vendor_averages(argument)
        elif argument == '-g': # grades data flag
            argument = arguments.pop(0) # pop again to get data file
            vendor_grades(argument)
        elif argument == '-s': # score and decision data flag
            argument = arguments.pop(0) # pop again to get data file
            score_vendors(argument)
        elif argument == '-o': # table outfile flag
            argument = arguments.pop(0)
            grade_to_Out(argument)
        elif argument == '-h':
            usage(0)

if __name__ == '__main__':
    main()
