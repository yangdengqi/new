# -*- coding: utf-8 -*-
"""
@author: 楊登棋
"""
import requests
from bs4 import BeautifulSoup

def song_scraping(url):
    articles = []
    r = requests.get(url=URL, cookies={"over18":"1"})
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find("a"):
            href = tag.find("a")["href"]
            title = tag.find("a").text
            
            r2=requests.get(url=""+href, cookies={"over18":"1"}) #網址輸入
            soup2 = BeautifulSoup(r2.text, "lxml")
            articles.append({"title":title, "href":href, "text":soup2.text})
    return articles

#pip install jieba
import jieba.posseg # https://github.com/fxsjy/jieba
import time

for i in range(): #歌詞網址範圍
    URL = "" % i  #引用i當網址
    print("URL", URL)
    articles = song_scraping(url=URL)
    for article in articles:    
        filename = article["href"].split("/")[-1]
        print("full-href", URL[:50] + article["href"])

        with open(file="Cat/"+filename+".txt", mode="w", encoding="utf8") as file1:
            tagged_words = jieba.posseg.cut(article["text"])
            words = [word for word, pos in tagged_words]
            file1.write(" ".join(words))
            print(" ".join(words).strip()[:22])
        
#       print("title", list(tagged_words)[4:9])#article["title"])
    time.sleep(3)