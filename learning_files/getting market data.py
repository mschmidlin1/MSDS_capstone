import requests
from configs import TICKERS
from my_secrets import ALPACA_API_BASE_URL, PAPER_API_ID, PAPER_SECRET_KEY, POLYGON_API_KEY
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data import StockDataStream
from polygon import RESTClient
from polygon.rest import models
from datetime import datetime
import pandas as pd

tickers_list = list(TICKERS.values())

# tickers_list = ["SPY"]



# stock_stream = StockDataStream(PAPER_API_ID, PAPER_SECRET_KEY)
# # async handler
# async def quote_data_handler(data):
#     # quote data will arrive here
#     print(data)

# stock_stream.subscribe_quotes(quote_data_handler, "SPY")

# stock_stream.run()






# print("++++++++Quote info from ALPACA++++++++++++++")
# print()

client = StockHistoricalDataClient(PAPER_API_ID, PAPER_SECRET_KEY)
# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols='BTC/USD')

# latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

# print(latest_multisymbol_quotes['BTC/USD'])
# for ticker in tickers_list:
#     print("*"*80)
#     print(ticker)
#     print(latest_multisymbol_quotes[ticker])
#     print("*"*80)
#     print()
#     print()

# print("++++++++++++++++++++++"*2)



# print()
# print()
# print()
# df = bars.df

# print(df.head())
# print(df.shape)
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

# no keys required for crypto data
# client = StockHistoricalDataClient()

request_params = StockBarsRequest(
                        symbol_or_symbols="AAPL", #"ETH/USD"],
                        timeframe=TimeFrame.Minute,
                        start=datetime(year=2022, month=7, day=1, hour=0, minute=0, second=0),
                        end=datetime(year=2022, month=7, day=2, hour=0, minute=0, second=0)
                 )

bars = client.get_stock_bars(request_params)

# convert to dataframe
print(type(bars.df))
print("++++++++++++++++++++++"*2)