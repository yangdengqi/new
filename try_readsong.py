# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#pip install jieba
#import jieba.posseg # https://github.com/fxsjy/jieba

def song_scraping(url):
    articles = []
    r1 = requests.get(url=URL2)
    options = Options()
    options.add_argument("--disable-popup-blocking")
    
    soup = BeautifulSoup(r1.text, "lxml")
    tag_lis = soup.find_all("li", class_="clearfix")
    for tag in tag_lis:
        if tag.find("a"):
            href2 = tag.find("a")["href"]
            #title = tag.find("a").text
            
            r2=requests.get(url="https://www.appleofmyeye.com.tw/"+href2)
            options = Options()
            options.add_argument("--disable-popup-blocking")
            
            soup2 = BeautifulSoup(r2.text, "lxml")
            for link in soup2.select('.geciInfo'):
                articles.append({"text": link.text , "song": soup2.select('h1')[0].text})
    return articles

#pip install jieba
import jieba.posseg # https://github.com/fxsjy/jieba
import time

URL1 = ["https://www.appleofmyeye.com.tw/geshou/dalunan-all-all.htm",
        "https://www.appleofmyeye.com.tw/geshou/dalunv-all-all.htm",
        "https://www.appleofmyeye.com.tw/geshou/daluzuhe-all-all.htm",
        "https://www.appleofmyeye.com.tw/geshou/gangtainan-all-all.htm",
        "https://www.appleofmyeye.com.tw/geshou/gangtainv-all-all.htm",
        "https://www.appleofmyeye.com.tw/geshou/gangtaizuhe-all-all.htm"]

#全部歌手跑完跑到上面列表
import os
#www=URL1[1]
for www in URL1:
#if www == URL1[1]:
    r = requests.get(url=www)
    options = Options()
    options.add_argument("--disable-popup-blocking")
    soup = BeautifulSoup(r.text, "lxml")
    for singer in soup.select(".singerList"):
        for tag in singer.select("li"):
            if tag.find("a"):
                href = tag.find("a")["href"]
                URL2="https://www.appleofmyeye.com.tw/"+href
                print("URL2:",URL2)
                
                articles = song_scraping(url=URL2)
                #print(articles)
                
                for article in articles:    
                    
                    filename = article["song"].replace("\t","")
                    filename = filename.replace("/","")
                    #print(filename)
                    tagged_words = jieba.posseg.cut(article["text"])
                    words = [word for word, pos in tagged_words]
                    if www == URL1[0]:
                        file = "china/china_boy/%s.txt" %filename
                        if not os.path.exists(file):
                            with open(file , mode="w", encoding="utf8") as file1:
                                print(" ".join(words),file=(file1))
                                #print(" ".join(words).strip())
                                print("ok")
                            if not os.path.getsize(file):
                                os.remove(file)
                            time.sleep(1)
                    elif www == URL1[1]:
                        file = "china/china_girl/%s.txt" %filename
                        if not os.path.exists(file):
                            with open(file, mode="w", encoding="utf8") as file2:
                                print(" ".join(words),file=(file2))
                                #print(" ".join(words).strip()[:22])
                                print("ok")
                            if not os.path.getsize(file):
                                os.remove(file)
                            time.sleep(1)
                    elif www == URL1[2]:
                        file = "china/china_team/%s.txt" %filename
                        if not os.path.isfile(file):
                            with open(file , mode="w", encoding="utf8") as file3:
                                print(" ".join(words),file=(file3))
                                #print(" ".join(words).strip()[:22])
                                print("ok")
                            if not os.path.getsize(file):
                                os.remove(file)
                            time.sleep(1)
                    elif www == URL1[3]:
                        file = "taiwan/taiwan_boy/%s.txt" %filename
                        if not os.path.isfile(file):
                            with open(file , mode="w", encoding="utf8") as file4:
                                print(" ".join(words),file=(file4))
                                #print(" ".join(words).strip()[:22])
                                print("ok")
                            if not os.path.getsize(file):
                                 os.remove(file)
                            time.sleep(1)
                    elif www == URL1[4]:
                        file = "taiwan/taiwan_girl/%s.txt" %filename 
                        if not os.path.isfile(file):
                            with open(file, mode="w", encoding="utf8") as file5:
                                print(" ".join(words),file=(file5))
                                #print(" ".join(words).strip()[:22])
                                print("ok")
                            if not os.path.getsize(file):
                                os.remove(file)
                            time.sleep(1)
                    elif www == URL1[5]:
                        file = "taiwan/taiwan_team/%s.txt" %filename
                        if not os.path.isfile(file):
                            with open(file, mode="w", encoding="utf8") as file6:
                                print(" ".join(words),file=(file6))
                                #print(" ".join(words).strip()[:22])  
                                print("ok")
                            if not os.path.getsize(file):
                                os.remove(file)
                            time.sleep(1)
                    else:
                        break
                time.sleep(3)
