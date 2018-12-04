import pandas as pd 
import matplotlib.pyplot as plt 

def get_max_close(symbol):
	""" Return the maximum closing value for stock indicated by symbol.

	Note: Data for a stock is stored in file: data/<symbol>.csv
	"""
	df = pd.read_csv('data/{}.csv'.format(symbol))
	return df['Close'].max()

def test_run():
	df = pd.read_csv('data/AAPL.csv')
	print df.tail()
	print df[10:21] # Rows between 10 and 20 !!! not 10 to 21

def test_run_2():
	for symbol in ['AAPL', 'IBM']:
		print "Max close"
		print symbol, get_max_close(symbol)

def test_run_3():
	df = pd.read_csv('data/AAPL.csv')
	print df['Adj Close']
	df[['Close', 'Adj Close']].plot()
	plt.show()

if __name__ == '__main__':
	test_run_3()