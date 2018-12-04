import pandas as pd

def test_run():
	#Define date range
	start_date = '2010-01-22'
	end_date = '2010-01-26'
	dates = pd.date_range(start_date, end_date)
	#print dates[0]

	#Create an empty dataframe
	df1 = pd.DataFrame(index=dates)
	#print df1

	#Read SPY data into temporary dataframe
	dfSPY = pd.read_csv('data/SPY.csv', index_col='Date',\
						parse_dates=True, usecols=['Date', 'Adj Close'],\
						na_values=['nan'])
	dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

	#Join the two dataframes using DataFrame.join()
	df1 = df1.join(dfSPY, how='inner')

	#Read in more stocks
	symbols = ['GOOG', 'AAPL', 'GLD']

	for symbol in symbols:
		dftemp = pd.read_csv('data/{}.csv'.format(symbol), index_col='Date',\
							parse_dates=True, usecols=['Date', 'Adj Close'],\
							na_values=['nan'])
		dftemp = dftemp.rename(columns={'Adj Close': symbol})
		df1 = df1.join(dftemp, how='left')

	print df1

if __name__ == '__main__':
	test_run()