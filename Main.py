from Tweet import getTwitterPics
from Flickr import getFlickrPics

def main():
    print("Flickr Information")
    getFlickrPics("#dctech")
    print("\nTwitterInformation\n")
    getTwitterPics("dctech")

if __name__ == '__main__':
    main()