
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

news_urls = [
    "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en",
    "https://www.cnn.com/",
    "https://www.nbcnews.com/",
    "https://www.foxnews.com/",
    "https://apnews.com/",
    "https://www.vox.com/",
    "https://time.com/",
    "https://www.washingtonpost.com/",
    "https://www.usatoday.com/",
    "https://abcnews.go.com/",
    "https://www.wsj.com/news/world?gclid=Cj0KCQiA6rCgBhDVARIsAK1kGPJMbSU0Bd_RBeUkLv3YVhPk6G0yc9cZiVGv7FFrXKyH2-jFcIjZbq4aAumbEALw_wcB&mod=djmc_DGWorld&gclsrc=aw.ds&ef_id=YNEdOwAAABkp53MD:20230312011148:s",
    "https://www.npr.org/sections/news/",
    "https://www.usnews.com/",
    "https://www.nytimes.com/"]

import logging
def set_logger():
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # logging.getLogger().addHandler(logging.StreamHandler())

