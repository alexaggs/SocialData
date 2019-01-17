import flickr_api
import time
from datetime import datetime
from Utility import Utility

key = "key"
secret = "key"

flickr_api.set_keys(key, secret)

def getFlickrPics(hashtag, dateChosen):
    pics = []

    #Converting from datetime to unix timestamps
    date = dateChosen
    unixTimeToday = time.mktime(date.timetuple())
    monthAgo = Utility.dateConversion(date, 31)
    unixTimeMonthAgo = time.mktime(monthAgo.timetuple())

    photos = flickr_api.Photo.search(tags=hashtag, min_upload_date=unixTimeMonthAgo, max_upload_date=unixTimeToday)

    for p in photos:
        pics.append(p)

    pics.sort(key=lambda r: r.comments, reverse=True)

    for p in pics:
        print(p.description.encode("utf-8") + " " + str(p.comments).encode("utf-8"))