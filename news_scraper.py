import requests
from bs4 import BeautifulSoup
from details_extractor import details_extractor
from main import insert_news_db
import json

news_links=[]

for i in range(1,2):
    print(i)
    URL = "https://timesofindia.indiatimes.com/india/delhi"
    if i>1:
        URL+="/"+str(i)
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="c_articlelist_stories_2")
    # print(results)
    news_link_elements = results.find_all("a")
    for i, link in enumerate(news_link_elements):
        news_links.append("https://timesofindia.indiatimes.com" + link.get('href'))

print(len(news_links))

for i,news_link in enumerate(news_links):
    print(i+1)
    try:
        art_url = news_link
        page = requests.get(art_url)
        soup = BeautifulSoup(page.content, "html.parser")
        div_text=soup.find_all("div",{'class': '_s30J clearfix'});
        news_art = div_text[0]
        news_details = json.loads(details_extractor(news_art.text))
        news_details["article_content"]=news_art.text
        print(news_details["article_content"])
        if "IsRelatedToRoadAccident" in news_details and news_details["IsRelatedToRoadAccident"]==True:
            print("IT IS RELATED TO ROAD ACCIDENT")
            insert_news_db(news_details)
    except Exception as e:
        print(e)
        print("Error")