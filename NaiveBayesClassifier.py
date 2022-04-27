from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
import random

n = 300

china_dir = "china/china_boy/"
pcr1 = PlaintextCorpusReader(root=china_dir, fileids=".*\.txt")

c = "china"
china_documents = [(pcr1.words(fileid),c) for fileid in pcr1.fileids()]
#print(china_documents[:9])

taiwan_dir = "taiwan/taiwan_boy/"
pcr2 = PlaintextCorpusReader(root=taiwan_dir, fileids=".*\.txt")

c = "taiwan"
taiwan_documents = [(pcr2.words(fileid),c) for fileid in pcr2.fileids()]
#print(taiwan_documents[:9])

documents = china_documents + taiwan_documents
print(documents[0])
print(documents[-1])

random.shuffle(x=documents) # Different results each time?

import datetime
print(datetime.datetime.now())

N_features = 2000
all_words = FreqDist(pcr1.words() + pcr2.words())   # 20 seconds...
word_features = list(all_words)[:N_features]


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

print(classifier.show_most_informative_features(5))

# What are the most informative training features in your PTT text prediction task? 
# do they make sense to you?
