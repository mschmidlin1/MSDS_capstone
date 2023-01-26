from alpaca.trading.client import TradingClient
from my_secrets import ALPACA_API_BASE_URL, PAPER_API_ID, PAPER_SECRET_KEY
trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY, paper=True)
# attempt to cancel all open orders
cancel_statuses = trading_client.cancel_orders()

print(type(cancel_statuses))
print(cancel_statuses)