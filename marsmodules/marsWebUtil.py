"""
This module is a collection of mars web utilities
"""

import pywhatkit as kit
import wikipedia as wiki
import requests
from bs4 import BeautifulSoup

"""
This function contains the pywhatkit which has a method of playonyt that automatically redirects and play the provided string in the function.

To learn more about the pywhatkit visit here: https://pypi.org/project/pywhatkit/
"""
def playOnYoutube(text):
    play = text.replace('youtube', '')
    kit.playonyt(play)


def searchInfo(text):
    try:
        print(text)
        summary = wiki.summary(text, sentences=2)
        return summary
    except:
        return 'Error finding answer. Try again!'


"""
This is a function that web srapes using the bs4 module.
You can view the documentation of the bs4 here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
def getLocalNews():
    """
    This method web scrape from the website cnnphilippines that contains local news healines and return a formated string

    return <string>
    """
    local_news_html = requests.get('https://www.cnnphilippines.com/news/').text
    soup = BeautifulSoup(local_news_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"Headline: {headline}; {article}"


def getGlobalNews():
    """
    This method is also web scraped in cnnphllipines a return a formated string containing the data

    return <string>
    """
    global_news_html = requests.get('https://www.cnnphilippines.com/world/').text
    soup = BeautifulSoup(global_news_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"Headline: {headline}; {article}"


def getShowbizNews():
    showbiz_html = requests.get('https://www.cnnphilippines.com/entertainment/').text
    soup = BeautifulSoup(showbiz_html, 'html.parser')

    news_article = soup.find('div', class_="col-sm-4")

    headline = news_article.find('a').text

    article_div = news_article.find('div', class_="slider-text")

    article = article_div.find('p').text

    return f"{headline}; {article}"
    

"""
This code below is used to test these functions created above.
inside the if statement, the code will only be executed when the module itself is run.
Otherwise will not execute
"""
if __name__ == "__main__":
    getShowbizNews()