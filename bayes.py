import nltk
import re
import pandas as pd
import twitter as t
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from json import dumps

xlsx = pd.ExcelFile('Tweets_Mg.xlsx')
df = pd.read_excel(xlsx, 'sheet')
training_tweets = []
classes = []

for i in df.itertuples():
	training_tweets.append(i.text)
	classes.append(i.classificacao)

# training_tweets = ['feliz', 'alegre', 'chorando', 'amando', 'amo', 'triste', 'muito', 'amor']
# classes = [1, 0, -1, 1, 1, -1, 0, 1]

vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(training_tweets)
modelo = MultinomialNB()

# training database
modelo.fit(freq_tweets,classes)

def setKeyword(data):
	positive = negative = neutral = 0
	
	freq_tests = vectorizer.transform(data)
	for i in modelo.predict(freq_tests):
		score_positive = {}
		score_negative = {}
		score_neutral  = {}
		if i == 0:
			neutral = neutral + 1
		elif i == 1:
			positive = positive  + 1
		else:
			negative = negative + 1

	return  positive, negative, neutral
		












