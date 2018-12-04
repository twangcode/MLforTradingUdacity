import fix_yahoo_finance as fyf
import pandas_datareader.data as pdr
from datetime import datetime
import sys

# To use fix_yahoo_finance:
fyf.pdr_override()

def get_single_quote(symbol,start_date, end_date=datetime.today()):
        try:
        	data = pdr.get_data_yahoo(symbol, start_date, end_date)
        except:
        	print 'wrong input'
        	sys.exit(2)
        return data

def get_multi_quote(symbol_list, start_date, end_date):
        data_dict = {}
        for symbol in symbol_list:
                data_dict[symbol] = get_single_quote(symbol, start_date, end_date)
        return data_dict

def write_to_csv(symbol_list, start_date, end_date=datetime.today()):
        for symbol in symbol_list:
                data = get_single_quote(symbol, start_date, end_date)
                data.to_csv('{}.csv'.format(symbol))

start_date = datetime(2000,1,1)
end_date = datetime.today()

symbol_list = ['AAPL', 'GOOG', 'SPY', 'GLD', 'IBM']
write_to_csv(symbol_list, start_date, end_date)

