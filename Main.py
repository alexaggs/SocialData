from Tweet import getTwitterPics
from Flickr import getFlickrPics
from datetime import datetime

def main():
    print("Flickr Information")
    getFlickrPics("#dctech", datetime.today())
    print("\nTwitterInformation\n")
    getTwitterPics("#dctech")

if __name__ == '__main__':
    main()