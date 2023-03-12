from requests_html import HTMLSession

session = HTMLSession()

url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

r = session.get(url=url)

r.html.render(sleep=1, scrolldown=0)


articles = r.html.find('article')

news_articles = {
    'headline': [],
    'link': [],
    'date': [],
}

for item in articles:
    # newsitem = item.find('h4', first=True)
    # title = newsitem.text
    newsitem1 = item.find('a', first=True)
    link = newsitem1.absolute_links
    title = newsitem1.text
    print(title)
    print(link)
    break