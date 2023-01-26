from my_secrets import ALPACA_API_BASE_URL, PAPER_API_ID, PAPER_SECRET_KEY

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, OrderStatus, QueryOrderStatus

trading_client = TradingClient(ALPACA_API_BASE_URL, PAPER_API_ID, paper=True)

# params to filter orders by
request_params = GetOrdersRequest(status=QueryOrderStatus.OPEN,)

# orders that satisfy params
orders = trading_client.get_orders(filter=request_params)