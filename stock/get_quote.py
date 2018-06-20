import pandas_datareader as pdr
from datetime import datetime

def get_single_quote(symbol,start_date, end_date):
        data = pdr.get_data_yahoo(symbols = symbol, start = start_date, end = end_date)
        return data

def get_multi_quote(symbol_list, start_date, end_date):
        data_dict = {}
        for symbol in symbol_list:
                data_dict[symbol] = get_single_quote(symbol, start_date, end_date)
        return data_dict

def write_to_csv(data_dict):
        for symbol in sorted(data_dict.keys()):
                data_dict[symbol].to_csv('{}.csv'.format(symbol))
        
        

start_date = datetime(2000,1,1)
end_date = datetime.today()

symbol_list = ['AAPL', 'GOOG', 'SPY', 'GLD']
write_to_csv(get_multi_quote(symbol_list, start_date, end_date))

