


from my_secrets import PAPER_API_ID, PAPER_SECRET_KEY

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.models import Order
import time



trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY, paper=True)
account = trading_client.get_account()
before = float(account.buying_power)
print(f"Buying power before trade: {float(before):,}")

market_order_data = MarketOrderRequest(
                      symbol="pooooop",
                      notional=2000,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )

market_order = trading_client.submit_order(market_order_data)
account = trading_client.get_account()
print(f"Buying power after trade: {float(account.buying_power):,}")
print(type(market_order))
print(market_order.failed_at)
print(market_order.filled_at)
print(market_order.status)
print(market_order.status)