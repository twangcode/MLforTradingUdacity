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
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')
    
    # Compute rolling mean using a 20-day window
    # rolling_mean has been deprecated
    # use dataframe.rolling() function
    rm_SPY = df.rolling(window=20).mean()

    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()
    


if __name__ == "__main__":
    test_run()
