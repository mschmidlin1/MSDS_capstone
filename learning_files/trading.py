import os
import sys

sys.path.append(os.getcwd())

from my_secrets import PAPER_API_ID, PAPER_SECRET_KEY

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.models import Order

# paper=True enables paper trading
trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY, paper=True)
account = trading_client.get_account()

print(f"Buying power before trade: {float(account.buying_power):,}")


market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )

market_order = trading_client.submit_order(market_order_data)

# print(dir(Order))
# for property_name, value in market_order:
#     print(f"\"{property_name}\": {value}")
import time

account = trading_client.get_account()
time.sleep(2)
print(f"Buying power after trade: {float(account.buying_power):,}")