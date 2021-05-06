#!/usr/bin/env python3

import csv
import sys
from collections import defaultdict
from collections import OrderedDict
from funcs import single_vendor
from funcs import print_vendor_data

def main():
    arguments = sys.argv[1:]
    while arguments:
        argument = arguments.pop(0)
        if argument == '-s':
            argument = arguments.pop(0)
            vendor = arguments.pop(0)
            vendor_dict = single_vendor(argument, vendor)
            print_vendor_data(vendor_dict)
    
if __name__ == '__main__':
    main()
