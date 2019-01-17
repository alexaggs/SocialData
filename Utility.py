from datetime import timedelta

class Utility(object):

    # Calculates a month ago from today
    @staticmethod
    def dateConversion(date, d):
        return date - timedelta(days=d)