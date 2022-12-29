
from configs import PAPER_API_ID, PAPER_SECRET_KEY

from alpaca.trading.client import TradingClient

# paper=True enables paper trading
trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY)
account = trading_client.get_account()

print(type(account))
print(account)
print()
print(f"Buying power: {int(account.buying_power)}")
print(f"cash: {int(account.cash)}")
print(f"portfolio value: {int(account.portfolio_value)}")

