#Basic utility class to utilize shared methods

from datetime import timedelta

class Utility(object):

    # Calculates however many days back from today
    @staticmethod
    def dateConversion(date, d):
        return date - timedelta(days=d)