# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:24:32 2022

@author: 楊登棋
"""

from wordcloud import WordCloud
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
        """a = f.readlines()
        for song_words in a:
            words+=song_words.split()
            
            count = {}
            for word in song_words:
                if word not in stopwords[0:] and word:
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
            words_count.append(count)"""
           
        b = f.read().split()
        count = {}
        for all_word in b:
            if all_word not in stopwords[0:]:               
                if all_word in count:
                    count[all_word] += 1
                else:
                    count[all_word] = 1
        dic=sorted(count.items(), key=operator.itemgetter(1),reverse=True)
        
        words_count.append(dic[0:20])
for i in range(7):
    print(words_count[i],'\n')
    
