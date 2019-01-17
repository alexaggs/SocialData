#The purpose of this class is to use code from a GitHub project to obtain tweets from a month ago.
#I was not able to do this because of the Twitter API limititations, so this is able to take care of that
#except I am not able to check if the tweet contains a photo at all, hence I can't return a photo here like I can with the Twitter API.
#Just wanted to show both sides of the issues I was having

#Code Used: https://github.com/Jefferson-Henrique/GetOldTweets-python

import GetOldTweets3
from Utility import Utility
from datetime import datetime, timedelta

today = datetime.today()

tweetCriteria = GetOldTweets3.manager.TweetCriteria().setQuerySearch("#dctech").setSince(Utility.dateConversion(today, 31).strftime("%Y-%m-%d")).setUntil(today.strftime("%Y-%m-%d"))
tweet = GetOldTweets3.manager.TweetManager.getTweets(tweetCriteria)

tweet.sort(key=lambda r: r.retweets, reverse=True)

for i in range(len(tweet)):
    print(tweet[i].text + " has " + str(tweet[i].retweets) + " retweets and was created on " +  str(tweet[i].date) + "\n")