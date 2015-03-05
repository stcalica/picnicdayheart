#!/bin/bash/python

__author__= "Kyle Calica & Adrian Cacho"

import tweepy
from tweepy.streaming import StreamListener

consumer_key = "8jbtWe9xKzrM051Tmb0c81ZM2"
consumer_secret = "SvNfaCbgDUmXb9GCnrmH9zcjl8ti0SeDRs0E20czTbl4dkL3F4" 
access_token =  "2908852254-C9XMN5yYXllfBNWkRxBV763zqm9sHdFVomPY1JN"
access_token_secret = "59U0HJbeynWosAbgtTgDGvXaviQajVIhN8xsdBp81aE1x"  


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print "Trying the Search Method now: \n"

q = raw_input("Enter Hashtag: ")

"""
tweets = api.search(q)

for tweet in tweets:
     print tweet.user.name + " : " + tweet.text
"""

#overriding the StreamListener class
class StdOutListener(StreamListener):
	
	def on_status(self, status):
		print(status.text)

# once we have an api object and a status listener we can create our stream object

myStreamListen = StdOutListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListen)
myStream.filter(track=[str(q)])

#http://tweepy.readthedocs.org/en/v3.3.0/streaming_how_to.html?highlight=streamming
#http://adilmoujahid.com/posts/2014/07/twitter-analytics/

#http://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/
#api.update_status("Eyy! Using Python to update my Twitter status #tweepy #python #programmingtest")


#create eventListner
#create log file
#possibly mysql database 
