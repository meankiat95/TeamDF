import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from webscrap.stopwords import stop_words, empty
from nltk.tokenize import word_tokenize
from filescrap.fileForensic import classification
import csv

import nltk

whitelist = ['title', 'p']

def checkPunkt():
    try:
        nltk.data.find('tokenizers/punkt')
        print("punkt exists")

    except:
        print("punkt not found, downloading now")
        nltk.download("punkt")

def openURLCSV(file_name):
    url_df = pd.read_csv(file_name)
    urls = (list(url_df.URL))
    return urls


def scrapeURL(urls):
    print('\n Scraping URLs ')
    article_list = []
    failed_list = []
    for url in urls:
        article_content = ""
        try:
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'lxml')
            page_content = [words for words in soup.find_all(text=True) if words.parent.name in whitelist]

            for stop in page_content:
                text_line = word_tokenize(stop)
                filtered_sentence = [w for w in text_line if w not in stop_words]
                for s in filtered_sentence:
                    if s in empty:
                        filtered_sentence.remove(s)
                if len(filtered_sentence) != 0:
                    filtered_sentence = ' '.join(filtered_sentence)
                    article_content += " " + filtered_sentence
                else:
                    pass

            article_content = article_content.lower()
            article_list.append(article_content)
            print("successfully scraped " + url)

        except:
            print("failed to scrape " + url)
            failed_list.append(url)
            pass

    both_list = [article_list, failed_list]
    return both_list


def urlAnalyze(url_list, extracted_content_list):
    count = 0
    urls = []
    categories = []
    print("\n URL CLASSIFICATION")
    for i in extracted_content_list:
        category = str(classification(i))
        url = str(url_list[count])
        print(category + " --- " + url)
        categories.append(category)
        urls.append(url)
        count += 1
    d = [categories, urls]
    return d


def failedURL(failed_urls):
    failed_scrape = []
    for i in range(0, len(failed_urls)):
        failed_scrape.append("Failed to scrape")
    f = [failed_scrape, failed_urls]
    return f


def resultsCSV(x, y):
    with open('URL Classification.csv', 'w+', encoding="ISO-8859-1", newline='') as file_csv:
        wr = csv.writer(file_csv)
        wr.writerow(("Category", "URL"))
        wr.writerows(x)
        wr.writerows(y)
    print("Results saved to URL Classification.csv")

