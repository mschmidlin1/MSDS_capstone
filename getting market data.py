import requests
from configs import ALPACA_API_BASE_URL, PAPER_API_ID, PAPER_SECRET_KEY, TICKERS
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data import StockDataStream

tickers_list = list(TICKERS.values())





stock_stream = StockDataStream(PAPER_API_ID, PAPER_SECRET_KEY)
# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

stock_stream.subscribe_quotes(quote_data_handler, "SPY")

stock_stream.run()







# client = StockHistoricalDataClient(PAPER_API_ID, PAPER_SECRET_KEY)
# multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=tickers_list)

# latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)



# for ticker in tickers_list:
#     print("*"*80)
#     print(ticker)
#     print(latest_multisymbol_quotes[ticker])
#     print("*"*80)
#     print()
#     print()
