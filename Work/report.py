# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    f = open(filename)
    lines = csv.reader(f)
    headers = next(lines)

    for fields in lines:
        holding_dict = {}
        try:
            #holding = (fields[0], int(fields[1]), float(fields[2]))
            holding_dict = {'name' : fields[0], 'shares' : int(fields[1]), 'price' : float(fields[2]) }
            portfolio.append(holding_dict)
        except ValueError as e:
            print("couldn't parse", fields)

    return portfolio


def read_prices():
    dict_prices = {}

    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        if row:
            dict_prices[row[0]] = float(row[1])

    return dict_prices

def gain_loss():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices()

    # Calculate the total cost of the portfolio
    total_cost = 0.0
    for s in portfolio:
        total_cost += s['shares']*s['price']

    print('Total cost', total_cost)

    # Compute the current value of the portfolio
    total_value = 0.0
    for s in portfolio:
        total_value += s['shares']*prices[s['name']]

    print('Current value', total_value)
    share_value = total_value - total_cost
    if(share_value < 0):
        print('Loss', share_value)
    else:
        print('Gain', share_value)
