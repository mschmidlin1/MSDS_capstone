
TIMEZONE="US/Eastern"
LOG_FILE_NAME = "logs/logs.txt"
ALPCA_API_BASE_URL = "https://paper-api.alpaca.markets"
TICKERS = {
    "APPLE_TICKER": "AAPL",
    "MICROSOFT_TICKER": "MSFT",
    "CORNING_TICKER": "GLW",
    "NVIDIA_TICKER": "NVDA",
    "AMD_TICKER": "AMD",
    }

import logging
def set_logger():
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

