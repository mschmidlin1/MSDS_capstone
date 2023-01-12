from alpaca.data import StockDataStream
from my_secrets import ALPACA_API_BASE_URL, PAPER_API_ID, PAPER_SECRET_KEY

# keys required
wss_client  = StockDataStream(ALPACA_API_BASE_URL, PAPER_API_ID)

# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "GLW")

wss_client.run()