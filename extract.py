"""Extract data on stock data from CSV and Stock API.

The `load_symbols` function extract stock symbols and some other
data from a CSV file into a collection.
"""
import requests
from models import Stock
from api_key import api_key


def load_stock_data(symbol):

    # Income statement
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    income_statement = r.json()

    # Balance Sheet
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    balance_sheet = r.json()

    # Cash flow
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    cash_flow = r.json()

    return Stock(symbol,balance_sheet, income_statement, cash_flow)






