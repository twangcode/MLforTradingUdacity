import pandas as pd 
import matplotlib.pyplot as plt 

from util import get_data, plot_data

def compute_daily_returns(df):
	daily_returns = df / df.shift(1) - 1
	daily_returns.ix[0,:] = 0 
	return daily_returns 

def test_run():
	# Read data
	dates = pd.date_range('2009-01-01', '2012-12-31')
	symbols = ['SPY']
	df = get_data(symbols, dates)
	# plot_data(df)

	# Compute daily returns
	daily_returns = compute_daily_returns(df)
	# plot_data(daily_returns, title="Daily Returns", ylabel="Daily returns")

	# Plot a histogram
	daily_returns.hist(bins=20)

	# Get mean and std
	mean = daily_returns['SPY'].mean()
	# print 'mean=', mean
	std = daily_returns['SPY'].std()
	# print 'std=', std

	plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
	plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
	plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
	plt.show()

	print daily_returns.kurtosis()


if __name__ == '__main__':
	test_run()
