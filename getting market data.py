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






print("++++++++Quote info from ALPACA++++++++++++++")
print()

client = StockHistoricalDataClient(PAPER_API_ID, PAPER_SECRET_KEY)
multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=tickers_list)

latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)


for ticker in tickers_list:
    print("*"*80)
    print(ticker)
    print(latest_multisymbol_quotes[ticker])
    print("*"*80)
    print()
    print()

print("++++++++++++++++++++++"*2)



print()
print()
print()



print("++++++++Bars info from ALPACA++++++++++++++")
print()

request_params = StockBarsRequest(
                        symbol_or_symbols=tickers_list,
                        timeframe=TimeFrame.Day,
                        start=datetime(year=2022, month=7, day=1),
                        end=datetime(year=2022, month=7, day=8)
                 )

bars = client.get_stock_bars(request_params)

df = bars.df

print(df.head())
print(df.shape)

print("++++++++++++++++++++++"*2)