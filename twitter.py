from TwitterSearch import *
import credentials as lc
import re
from pprint import pprint

tso = TwitterSearchOrder()
tso.set_language('pt')
ts = TwitterSearch(
      lc.Loadcredentials(0),
      lc.Loadcredentials(1), 
      lc.Loadcredentials(2), 
      lc.Loadcredentials(3)
    )
		
def remove_urls (text):
	text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
	return(text)

def ReadTweets(keywords_id):
	try:
			result = []
			c = 0
			tso.set_keywords([keywords_id])
			for tweet in ts.search_tweets_iterable(tso):
				if c <= 500:
					# print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']))
					result.append(remove_urls(tweet['text'].replace('@', '').replace('RT', '')))
				else:
					break
				c = c + 1		
	except TwitterSearchException as e:
			print(e)
	return result


