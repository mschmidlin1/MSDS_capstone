import time
from configs import TIMEZONE
import datetime
import pytz

TIMEZONE = 'US/Mountain'

class Market_Monitor():
    def __init__(self, trading_client, TIMEZONE):
        self.TIMEZONE = TIMEZONE
        self.trading_client = trading_client
        self.tzinfo = pytz.timezone(self.TIMEZONE)
        self.update()

    def current_dt(self):
        self.dt = datetime.datetime.now(self.tzinfo)

    def current_tod(self):
        self.current_dt()
        self.tod = self.dt.time()

    def get_trade_clock(self):
        self.trade_clock = self.trading_client.get_clock()

    def update(self):
        self.current_tod()
        self.get_trade_clock()
        self.market_open = self.trade_clock.is_open
        self.next_open = self.trade_clock.next_open
        self.next_close = self.trade_clock.next_close
        self.time_until_open = datetime.timedelta(minutes=0)
        if not self.market_open:
            self.time_until_open = self.next_open - self.dt

    def is_market_open(self):
        self.update()
        return self.market_open

    def market_closed_loop(self):
        time_to_sleep = self.time_remaining - datetime.timedelta(minutes=10)
        print(f"Sleeping for {time_to_sleep}.")#will change to a log eventually
        time.sleep(time_to_sleep.total_seconds())
        print(f"Waking up! Will now continually check until market is open.") #log eventually
        self.check_open_continuous()
    
    def check_open_continuous(self):
        while True:
            self.update()
            if self.market_open:
                break




if __name__ == "__main__":
    monitor = Market_Monitor(TIMEZONE)
    print("Current Time:", monitor.tod)
    print(monitor.is_market_open())

