#Retrieves photos within tweets up until the Twitter API limitations

import tweepy
from datetime import datetime
from TweetObject import TweetObject
from Utility import Utility

consumer_key = 'key'
consumer_secret = 'key'
access_token = 'key'
access_token_secret = 'key'

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
            if(containsPhoto(media)):
                tweets.append(TweetObject(tweet.text, tweet.retweet_count, tweet.created_at))

    #Sort by number of retweets per tweet
    tweets.sort(key=lambda r: r.numRetweets, reverse=True)

    for t in tweets:
        print(t.getText().encode("utf-8")  + " has " + str(t.getRetweets()).encode("utf-8") + " retweets and was created on " + str(t.getCreatedAt()) + "\n")

#Used to check if a current tweet contains a photo
def containsPhoto(media):
    return media.get("type", None) == "photo"

#Used to check if a status contains any sort of media, used for tweets that are not obtained via the Twitter API
def containsMedia(id):
    tweet = api.get_status(id).entities
    if 'media' in tweet:
        return True