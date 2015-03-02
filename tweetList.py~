#!/bin/bash/python

__author__= "Kyle Calica & Adrian Cacho"

import tweepy

consumer_key = "8jbtWe9xKzrM051Tmb0c81ZM2"
consumer_secret = "SvNfaCbgDUmXb9GCnrmH9zcjl8ti0SeDRs0E20czTbl4dkL3F4" 
access_token =  "2908852254-C9XMN5yYXllfBNWkRxBV763zqm9sHdFVomPY1JN"
access_token_secret = "59U0HJbeynWosAbgtTgDGvXaviQajVIhN8xsdBp81aE1x"  


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

user =  api.me()

print user.name
print str(user.location)



#http://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/
#api.update_status("Eyy! Using Python to update my Twitter status #tweepy #python #programmingtest")


public_tweets = api.home_timeline()
for tweet in public_tweets:
	print tweet.text

