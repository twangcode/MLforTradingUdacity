import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2013,1,27)

f = web.DataReader('F', 'google', start, end)
print f