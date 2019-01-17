#The purpose of this class is to use code from a GitHub project to obtain tweets from a month ago.
#This actually is able to complete the requirements, but does not always work because of the Twitter Rate Limits. Also, this s not compatable wth Python 2.7
#so I cant utilize this

#Code Used: https://github.com/Jefferson-Henrique/GetOldTweets-python

import GetOldTweets3
from Utility import Utility
from datetime import datetime
from Tweet import containsMedia

def getAllTweets(hashtag):
    today = datetime.today()

    tweetCriteria = GetOldTweets3.manager.TweetCriteria().setQuerySearch(hashtag).setSince(Utility.dateConversion(today, 31).strftime("%Y-%m-%d")).setUntil(today.strftime("%Y-%m-%d"))
    tweet = GetOldTweets3.manager.TweetManager.getTweets(tweetCriteria)

    tweet.sort(key=lambda r: r.retweets, reverse=True)

    for i in range(len(tweet)):
        if(containsMedia(tweet[i].id)):
            print(tweet[i].text + " has " + str(tweet[i].retweets) + " retweets and was created on " +  str(tweet[i].date) + "\n")
