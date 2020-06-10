# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename: str) -> dict:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    select = ['name', 'shares', 'price']

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    indices = [ headers.index(colname) for colname in select ]

    try:
        portfolio = [ { colname: row[index] for colname, index in zip(select, indices) }  for row in rows ]
    except ValueError as e:
        print(f"Row {rowno} Couldn't convert: {row}")

    #for rowno, row in enumerate(rows):
    #    record = dict(zip(headers, row))
    #    try:
            #stocks = {
            #        'name'  : record['name'],
            #        'shares' : int(record['shares']),
            #        'price' : float(record['price'])
            #}
            #portfolio.append(stocks)
        #except ValueError as e:
        #    print(f"Row {rowno} Couldn't convert: {row}")

    return portfolio


def read_prices(filename: str) -> dict:
    dict_prices = {}

    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        if row:
            dict_prices[row[0]] = float(row[1])

    return dict_prices

def calculate_total_gain_loss():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices()
    print(portfolio)
    type(portfolio)
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

def portfolio_report(portfolio, prices):
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)

    portfolio_with_change = []
    #Calculating Gaing/Loss
    for s in portfolio:
        portfolio_with_change.append((s['name'], s['shares'], prices[s['name']] , float(prices[s['name']]) - float(s['price'])))

    print_report(portfolio_with_change)

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    separator = '-' * 10 + ' '
    #Printing table
    print('%10s %10s %10s %10s' % headers)
    print(separator * len(headers))
    for name, shares, prices, change in report:
        prices_s = '$' + str(prices)
        print(f'{name:>10s} {shares:>10s} {prices_s:>10s} {change:>10.2f}')
