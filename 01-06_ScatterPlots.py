"""Scatter plots"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

from util import get_data, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df / df.shift(1) - 1
    daily_returns.ix[0,:] = 0
    return daily_returns

def test_run():
	# Read Data
	dates = pd.date_range('2009-01-01', '2012-12-31')
	symbols = ['SPY', 'AAPL', 'GLD']
	df = get_data(symbols, dates)

	# Compute daily returns:
	daily_returns = compute_daily_returns(df)

	# Scatterplot SPY vs AAPL
	daily_returns.plot(kind='scatter', x='SPY', y='AAPL')
	beta_AAPL, alpha_AAPL = np.polyfit(daily_returns['SPY'], daily_returns['AAPL'], 1)
	plt.plot(daily_returns['SPY'], beta_AAPL*daily_returns['SPY']+alpha_AAPL, '-', color='r')
	plt.show()

	daily_returns.plot(kind='scatter', x='SPY', y='GLD')
	beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['AAPL'], 1)
	plt.plot(daily_returns['SPY'], beta_GLD*daily_returns['SPY']+alpha_GLD, '-', color='r')
	plt.show()

	# Compute correcation:
	print daily_returns.corr(method='pearson')

if __name__ == '__main__':
	test_run()