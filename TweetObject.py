#Used to store the tweet and number of retweets

class TweetObject(object):
    text = "";
    numRetweets = 0;

    def __init__(self, text, numRetweets, createdAt):
        self.text = text;
        self.numRetweets = numRetweets;
        self.createdAt = createdAt;

    def getText(self):
        return self.text;

    def getRetweets(self):
        return self.numRetweets;

    def getCreatedAt(self):
        return self.createdAt;