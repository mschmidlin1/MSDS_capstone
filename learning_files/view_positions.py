
from my_secrets import PAPER_API_ID, PAPER_SECRET_KEY
from configs import ALPCA_API_BASE_URL
import requests

# endpoint = f"/v1/trading/accounts/{PAPER_API_ID}/positions"

# r = requests.get(ALPCA_API_BASE_URL+endpoint)

# print(r.status_code)








from alpaca.trading.client import TradingClient
trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY, paper=True)
# paper=True enables paper trading
positions = trading_client.get_all_positions()

print(positions)
print(type(positions))
for position in positions:
    for property_name, value in position:
        print(f"\"{property_name}\": {value}")
