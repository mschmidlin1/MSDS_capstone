#https://www.youtube.com/watch?v=9R7pCh4yCm8&t=350s
import alpaca_trade_api as tradeapi
from alpaca_trade_api import StreamConn

APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

API_ID = "PK92A2VGKAAR9WB08JLW"
SECRET_KEY = "xjsGTIqTaQpkWKBBNGjvIiRi5Mk75W0opie4gXWU"

class PythonTradingBot:
    def __init__(self):
        pass

        self.shares = 0
        self.price = 0
        self._current_price()
        self.value = self.shares*self.price

    
    
    def _run(self):
        pass
    
    
    def _current_price():
        pass #return and set in object the current price
    
    def _buy():
        pass #code for buying, update shares, price, and value
    def _sell():
        pass #code for selling, update shares, price, and value







def main():
    print('hello world')


if __name__=="__main__":
    main()
