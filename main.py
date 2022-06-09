from extract import load_stock_data
import pprint
PATH = 'stock_list.csv'


def main():

    # Extract data from API
    symbol = 'GNK'
    stock_data = load_stock_data(symbol)
    #pprint.pprint(stock_data.balance_sheets['quarterlyReports'][0]) # latest quarterlyReport
    # pprint.pprint(stock_data.balance_sheets['annualReports'][0]) # latest annualReport
    # print('${:,.2f}'.format(stock_data.get_current_cash()))
    print(f'Initial floor price of {symbol}: ${stock_data.get_initial_floor_price():.2f}')


if __name__ == '__main__':
    main()
