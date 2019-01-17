#Used to store the tweet and number of retweets

class TweetObject(object):
    text = "";
    numRetweets = 0;

    def __init__(self, text, numRetweets):
        self.text = text;
        self.numRetweets = numRetweets;

    def getText(self):
        return self.text;

    def getRetweets(self):
        return self.numRetweets;