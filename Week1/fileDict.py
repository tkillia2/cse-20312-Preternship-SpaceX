#!/usr/bin/env python3

# SpaceX Preternship Team -- Week 1 Determine how to store dummy data into a dictionary efficiently


import csv
import collections

csv_file = open('SpaceXData.txt')

csv_file = csv_file.readlines()[1:]

csv_reader = csv.reader(csv_file, delimiter = ',')

# Creating a default dictionary to create easy referencing to the totals needed

dictData =  collections.defaultdict(dict)
for row in csv_file:
	# Creating dictionary keys out of our column labels
	vendor, daysPastPO, lotSize, nonconUnits, failedUnits, cost = row.split(',')

	# Adjusting the cost data so it can be utilized as integer values
	cost = cost.rstrip('%\n')

	# Creating a dictionary within the dictionary of vendors so we can easy access any total data values for a certain vendor for any of the criteria needed
	# Each creates a total of all the values for the given vendor in the specific category that can be referenced using the method dictData[vendor]['CRITERIA']
	dictData[vendor]['daysPastPO'] = dictData[vendor].get('daysPastPO', 0) + int(daysPastPO)
	dictData[vendor]['lotSize'] = dictData[vendor].get('lotSize', 0) + int(lotSize)
	dictData[vendor]['nonconUnits'] = dictData[vendor].get('nonconUnits', 0) + int(nonconUnits)
	dictData[vendor]['failedUnits'] = dictData[vendor].get('failedUnits', 0) + int(failedUnits)
	dictData[vendor]['cost'] = dictData[vendor].get('cost', 0) + int(cost)

for key, value in dictData.items():
	print(key, value)


print('')
print('')

print(dict(dictData))



'''dictData = collections.defaultdict(dict)
for row in csv_reader:
	if row[5].endswith('%'):
		row[5] = row[5].rstrip('%')
	dictData[row[0]] = []
	dictData[row[0]].append(row[1:])

for key, value in dictData.items():
	print(key, value)

print(dictData)'''



'''for row in csv.DictReader(csv_file, fieldnames = row[0]):
	print(row)'''

'''with open('SpaceXData.txt', newline = '') as csv_file:
	data = csv.DictReader(csv_file, delimiter = ',')
	for row in data:
		print(row) '''


