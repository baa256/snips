import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

end = dt.datetime.now()
start = end - dt.timedelta(days=365)

# # Get data for a single ticker
# # df = pdr.DataReader('AAPL', 'yahoo', start, end)


# # Get data for multiple tickers
# tickers = ['AAPL', 'MSFT', 'GOOG', 'TSLA']
# df = pdr.DataReader(tickers, 'yahoo', start, end)

# # Get data for multiple tickers and multiple fields
# # fields = ['Open', 'High', 'Low', 'Close', 'Volume']
# # df = pdr.DataReader(tickers, 'yahoo', start, end)[fields]

df = pdr.DataReader('TSLA', 'yahoo', start, end
