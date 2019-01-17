import flickr_api
import time
from datetime import datetime
from Utility import Utility

key = "9d0358bdb316fb63337122f6d5f8a8a5"
secret = "6b33cdb8f950b78a"

flickr_api.set_keys(key, secret)

def getFlickrPics(hashtag):
    pics = []

    #Converting from datetime to unix timestamps
    today = datetime.today()
    unixTimeToday = time.mktime(today.timetuple())
    monthAgo = Utility.dateConversion(today, 31)
    unixTimeMonthAgo = time.mktime(monthAgo.timetuple())

    photos = flickr_api.Photo.search(tags=hashtag, min_upload_date=unixTimeMonthAgo, max_upload_date=unixTimeToday)

    for p in photos:
        pics.append(p)

    pics.sort(key=lambda r: r.comments, reverse=True)

    for p in pics:
        print(p.description + " " + str(p.comments))