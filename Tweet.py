import tweepy
from datetime import datetime
from TweetObject import TweetObject
from Utility import Utility

consumer_key = 'GTvnHEwckh5HdjVhCHrXhC5X8'
consumer_secret = 'YCEnOTJ55Kat9aySMbMnX4IbObiOntPtbEWJlEURatzA6aShLZ'
access_token = '869602481101254657-B5lPR0aJOSL9LQps6hc3wPdUlRhM2zG'
access_token_secret = 'XJsm2As76jegYXr3JDfBA7YqGy9fhtEdquDpD1K7xzDwf'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def getTwitterPics(hashtag):
    monthAgo = Utility.dateConversion(datetime.today(), 31)

    #Used to keep track of the tweets stored
    tweets = []

    for tweet in tweepy.Cursor(api.search,q=hashtag,
                               lang="en",
                               include_entities=True,
                               wait_on_rate_limit=True,
                               since=monthAgo.strftime("%Y-%m-%d")).items():
        for media in tweet.entities.get("media", [{}]):
            #Checking if the tweet contains a photo
            if(media.get("type", None) == "photo"):
                tweets.append(TweetObject(tweet.text, tweet.retweet_count))
                print("testing")

    #Sort by number of retweets per tweet
    tweets.sort(key=lambda r: r.numRetweets, reverse=True)

    for t in tweets:
        print(t.getText() + " has " + str(t.getRetweets()) + " retweets\n")

