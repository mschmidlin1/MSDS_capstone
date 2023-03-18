from newspaper import Article
import newspaper
import pandas as pd
import numpy as np
import datetime
import os
from configs import set_logger
set_logger()







def scrape_news_website(website_url):
    paper = newspaper.build(website_url)
    num_articles_found = len(paper.articles)
    #print("number found: ",num_articles_found)
    article_dict = {
        'headline': [],
        'publish_date': [],
        'content': [],
        'authors': [],
        'keywords': [],
        'summary': []
    }
    for i, paper_article in enumerate(paper.articles):
        print(f"{i+1}/{num_articles_found}", end="\r")
        try:
            article = Article(paper_article.url)
        except AttributeError as e:
            continue
        article.download()
        try:
            article.parse()
        except Exception as e:
            continue 
        article_dict['headline'].append(article.title)
        article_dict['publish_date'].append(article.publish_date)
        article_dict['content'].append(article.text)
        article_dict['authors'].append(article.authors)
        try:
            article.nlp()
            article_dict['keywords'].append(article.keywords)
            article_dict['summary'].append(article.summary)
        except Exception as e:
            article_dict['keywords'].append(np.nan)
            article_dict['summary'].append(np.nan)
        

    df = pd.DataFrame(article_dict)
    return df

def extract_names(news_urls):
    news_names = []
    for url in news_urls:
        if "www." in url:
            website_name = url.split(".")[1]
        else:
            website_name = url.split(".com")[0].split("//")[-1]
        news_names.append(website_name)
    return news_names



def scrape_websites(news_names, news_urls, save_file="data/news_data/news_data.pkl"):

    frames = []

    for i, (name, url) in enumerate(zip(news_names, news_urls)):
        print()
        print(f"Scraping data for {name} ({i+1}/{len(news_names)})")
        news_df = scrape_news_website(url)
        news_df['source'] = name
        news_df['url'] = url
        news_df['date_pulled'] = datetime.date.today().strftime("%m-%d-%y")
        print(f"Found {news_df.shape[0]} usable articles.")
        frames.append(news_df)

    if os.path.exists(save_file):
        old_df = pd.read_pickle(save_file)
        print(f"Previous number of rows: {old_df.shape[0]:,}")
        frames.insert(0, old_df)

    df = pd.concat(frames)
    df.reset_index(inplace=True, drop=True)

    df = df[~df.duplicated(subset=['headline', 'publish_date', 'content'], keep='first')] #remove duplicates (leave first instance of duplicate)
    print(f"New number of rows {df.shape[0]:,}")
    df.to_pickle(save_file)

def main():
    from configs import news_urls
    news_names = extract_names(news_urls)
    lookup = {name: url for name, url in zip(news_names, news_urls)}
    scrape_websites(news_names, news_urls, save_file="data/news_data/news_data.pkl")

if __name__ == "__main__":
    main()