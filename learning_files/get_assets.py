from my_secrets import PAPER_API_ID, PAPER_SECRET_KEY
from configs import TICKERS
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
tickers_list = list(TICKERS.values())
trading_client = TradingClient(PAPER_API_ID, PAPER_SECRET_KEY)

# search for crypto assets
search_params = GetAssetsRequest(asset_class='crypto') #us_equity

assets = trading_client.get_all_assets(search_params)

asset_tickers = {asset.symbol: asset.name for asset in assets}

print(asset_tickers)

# print(len(asset_tickers))

# for tick in tickers_list:
#     print(tick, tick in asset_tickers.values())