from alpaca.trading.client import TradingClient
from my_secrets import ALPACA_API_BASE_URL, PAPER_API_ID, PAPER_SECRET_KEY
trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY, paper=True)


clock = trading_client.get_clock()


print(clock.is_open)
print(type(clock.is_open))
print(clock.next_close)
print(type(clock.next_close))
print(clock.next_open)
print(type(clock.next_open))