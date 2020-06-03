# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio(filename):
    total_cost = 0

    f = open(filename)
    lines = csv.reader(f)
    headers = next(lines)

    for fields in lines:
        try:
            total_cost = total_cost + (int(fields[1]) * float(fields[2]))
        except ValueError as e:
            print("couldn't parse", fields)

    return total_cost

#Reading from the command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio(filename)
print('Total cost:', cost)
