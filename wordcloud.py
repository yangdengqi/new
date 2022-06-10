# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 21:29:46 2022

@author: 楊登棋
"""

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
#from collections import Counter
import operator
stopwords=[]
words=[]
words_count = []

files=["words/china_boy_songs.txt",
      "words/china_girl_songs.txt",
      "words/china_team_songs.txt",
      "words/taiwan_boy_songs.txt",
      "words/taiwan_girl_songs.txt",
      "words/taiwan_team_songs.txt",
      "words/total_songs.txt"]

with open(file="words/stop.txt",mode="r+",encoding="utf8") as stop:
    stopwords = stop.read().split()
for file in files:   
    with open(file=file,mode="r+",encoding="utf8") as f:
        a = f.read().split()
        count = {}
        for all_word in a:
            if all_word not in stopwords[0:]:               
                if all_word in count:
                    count[all_word] += 1
                else:
                    count[all_word] = 1
        dic=sorted(count.items(), key=operator.itemgetter(1),reverse=True)
        words_count=dict(dic)

    font = "C:/Windows/Fonts/MSJH.TTC"
    mask = np.array(Image.open("picture.jpg"))
    wordcloud = WordCloud(background_color="white",max_words=80,max_font_size=500,min_font_size=10,mode="RGB",mask=(mask),font_path=font)
    wordcloud.generate_from_frequencies(words_count)
    
    plt.figure(figsize=(6,6))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
    if file==files[0]:
        wordcloud.to_file("china_boy_songs_wordcloud.jpg")
        print("ok")
    elif file==files[1]:
        wordcloud.to_file("china_girl_songs_wordcloud.jpg")
        print("ok")
    elif file==files[2]:
        wordcloud.to_file("china_team_songs_wordcloud.jpg")
        print("ok")
    elif file==files[3]:
        wordcloud.to_file("taiwan_boy_songs_wordcloud.jpg")
        print("ok")
    elif file==files[4]:
        wordcloud.to_file("taiwan_girl_songs_wordcloud.jpg")
        print("ok")
    elif file==files[5]:
        wordcloud.to_file("taiwan_team_songs_wordcloud.jpg")
        print("ok")
    elif file==files[6]:
        wordcloud.to_file("total_word_wordcloud.jpg")
        print("ok")