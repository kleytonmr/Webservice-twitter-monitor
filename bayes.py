import nltk
import re
import pandas as pd
import twitter as t
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from json import dumps

# import dataset
# dataset = pd.read_csv('Tweets_Mg.csv')
# dataset.count()
# training_tweets = dataset['Text'].values
# classes = dataset['Classificacao'].values

training_tweets = ['feliz', 'alegre', 'chorando', 'amando', 'amo', 'triste', 'muito', 'amor']
classes = [1, 0, -1, 1, 1, -1, 0, 1]

vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(training_tweets)
modelo = MultinomialNB()

# training database
modelo.fit(freq_tweets,classes)

def setKeyword(key):
	positive = negative = neutral =0
	
	freq_tests = vectorizer.transform(t.ReadTweets(key))
	for i in modelo.predict(freq_tests):
		if i == 0:
			neutral = neutral + 1
		elif i == 1:
			positive = positive  + 1
		else:
			negative = negative + 1
	return  {'Neutral':neutral, 'Positive':positive, 'Negative': negative}
		












