#!/bin/bash/python

__author__= "Kyle Calica & Adrian Cacho"

import tweepy
import socket
import json

from tweepy.streaming import StreamListener

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

consumer_key = " "
consumer_secret = " " 
access_token =  " "
access_token_secret = " "  


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


print "Trying the Search Method now: \n"
q = raw_input("Enter Hashtag: ")



#overriding the StreamListener class
class StdOutListener(tweepy.StreamListener):
	
	def on_status(self, status):
		
		if(status.possibly_sensitive == False):
		
			raw = status.text
			text = raw.encode('utf-8')
			
			try:
				media = status.entities['media'][0]['media_url']
				url = json.dumps(media)
				media_url = url.strip(' " ')
				#gather = text + " | " + media_url
				#s.send(gather)
				s.send(media_url)
				print media_url
		
			except: 
				pass
		
		return True
# once we have an api object and a status listener we can create our stream object

myStreamListen = StdOutListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListen)
myStream.filter(track=[str(q)], async=True)
