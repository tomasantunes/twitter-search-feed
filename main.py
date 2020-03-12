import tweepy
import sys

auth = tweepy.OAuthHandler("API_KEY", "API_ACCESS_KEY")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

count = len(sys.argv)
query = sys.argv[1]
global exists
exists = False

public_tweets = api.home_timeline()
if (count == 2):
	for tweet in public_tweets:
		text = tweet.text.encode("utf8")
		if (query in text):
			exists = True
			print(text)
			print("------------------------------------------------")

	if (not exists):
		print("No results were found")
elif count == 3:
	for tweet in tweepy.Cursor(api.user_timeline, screen_name=sys.argv[2], tweet_mode="extended").items():
		text = tweet.full_text.encode("utf8")
		if (query in text):
			exists = True
			print(text)
			print("------------------------------------------------")
	if (not exists):
		print("No results were found")