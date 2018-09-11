import tweepy
import sys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_key, access_key)

api = tweepy.API(auth)

query = sys.argv[1]
global exists
exists = False

public_tweets = api.home_timeline()
for tweet in public_tweets:
	if (query in tweet.text):
		exists = True
		print(tweet.text)
		print("------------------------------------------------")

if (not exists):
	print("No results were found")