import os
import pandas as pd 
import matplotlib.pyplot as plt 

def symbol_to_path(symbol, base_dir='data'):
	"""Return CSV file path given ticker symbol."""
	return os.path.join(base_dir, '{}.csv'.format(str(symbol)))

def get_data(symbols, dates):
	'''Read stock data (adjusted close) for given symbols from CSV files.'''
	df = pd.DataFrame(index=dates)
	if 'SPY' not in symbols: #add SPY for reference, if absent
		symbols.insert(0, 'SPY')

	for symbol in symbols:
		dftemp = pd.read_csv(symbol_to_path(symbol), index_col='Date',\
							parse_dates=True, usecols=['Date', 'Adj Close'],\
							na_values=['nan'])
		dftemp = dftemp.rename(columns={'Adj Close':symbol})
		df = df.join(dftemp)
		if symbol == 'SPY':
			df = df.dropna(subset=['SPY'])

	return df

def plot_data(df, title='Stock prices'):
	'''Plot stock prices'''
	ax = df.plot(title=title)
	ax.set_xlabel("Date")
	ax.set_ylabel('Price')
	plt.show()

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    plot_data(df.ix[start_index:end_index, columns], title='Selected data')

def normalize_data(df):
	'''Normalize stock prices using the first row of the dataframe.'''
	df = df / df.ix[0,:]
	return df

def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY', 'AAPL', 'GOOG', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute global statistics for each stock
    print df.mean()
    print df.median()
    print df.std()



if __name__ == "__main__":
    test_run()
