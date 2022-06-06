'''相關度加去多餘字'''
from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
from string import printable
import random

import urllib
#https://raw.githubusercontent.com/stopwords-iso/stopwords-zh/master/stopwords-zh.txt
file = urllib.request.urlopen(url="file:///C:/Users/%E6%A5%8A%E7%99%BB%E6%A3%8B/Desktop/%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80/stop.html")
stopwords = file.read().decode("utf8").split()
#print(stopword)

n = 2000

china_dir = "china/china_boy/"
pcr1 = PlaintextCorpusReader(root=china_dir, fileids=".*\.txt")

c = "boy"
boy_documents = [(pcr1.words(fileid),c) for fileid in pcr1.fileids()]

taiwan_dir = "taiwan/taiwan_boy/"
pcr2 = PlaintextCorpusReader(root=taiwan_dir, fileids=".*\.txt")
boy_documents += [(pcr2.words(fileid),c) for fileid in pcr2.fileids()]


c = "girl"
china_dir = "china/china_girl/"
pcr3 = PlaintextCorpusReader(root=china_dir, fileids=".*\.txt")
girl_documents = [(pcr3.words(fileid),c) for fileid in pcr3.fileids()]

taiwan_dir = "taiwan/taiwan_girl/"
pcr4 = PlaintextCorpusReader(root=taiwan_dir, fileids=".*\.txt")
girl_documents += [(pcr4.words(fileid),c) for fileid in pcr4.fileids()]


"""
china_dir = "china/china_girl/"
pcr5 = PlaintextCorpusReader(root=china_dir, fileids=".*\.txt")
team_documents = [(pcr5.words(fileid),c) for fileid in pcr5.fileids()]

taiwan_dir = "taiwan/taiwan_girl/"
pcr6 = PlaintextCorpusReader(root=taiwan_dir, fileids=".*\.txt")
team_documents += [(pcr6.words(fileid),c) for fileid in pcr6.fileids()]
"""
documents = boy_documents + girl_documents
print(documents[0])
print(documents[-1])

random.shuffle(x=documents) 

import datetime
print(datetime.datetime.now())


N_features = 5000
all_words = FreqDist(pcr1.words() + pcr2.words() + pcr3.words() + pcr4.words())   # 20 seconds...
aws = [word for word,freq in all_words.most_common(n=n) if word not in stopwords and word[0] not in printable]
word_features = list(aws)[:N_features]


def document_features(document_words):
    document_words = set(document_words)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features
#print(document_features(documents[0][0]))

N_testing = 100
print(datetime.datetime.now())
featuresets = [(document_features(d), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]

from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)  #分類模型
#print(datetime.datetime.now())
from nltk import classify
print(classify.accuracy(classifier, test_set))

print(classifier.show_most_informative_features(10))
