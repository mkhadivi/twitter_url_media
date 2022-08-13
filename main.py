import sys
import requests
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from bs4 import BeautifulSoup

## authentication
# twitter API 
# CONSUMER_KEY = #ENTER_YOUR_CONSUMER_KEY
# CONSUMER_SECRET = #ENTER_YOUR_CONSUMER_TOKEN
# ACCESS_KEY = #ENTER_YOUR_ACCESS_KEY
# ACCESS_SECRET = #ENTER_YOUR_ACCESS_TOKEN

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

if __name__ == "__main__":

    tweet_id = sys.argv[1]

    tweet = api.get_status(id=tweet_id)

    if hasattr(tweet, "entities"):
        if "urls" in tweet.entities.keys():
            url = tweet.entities['urls'][0]['expanded_url']
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')

            meta = soup.find_all('meta', {'name':'twitter:image:src'})
            if len(meta) == 0:
                meta = soup.find_all('meta', {'property':'og:image'})

            media_url = meta[0].attrs['content']
            media_file = requests.get(media_url)
            ext = media_url.split('.')[-1]
            file_name = str(tweet_id) + '_1.' + ext

            with open(file_name , 'wb') as dl_file:
                dl_file.write(media_file.content)
                            
    if hasattr(tweet, "extended_entities"):
        if "media" in tweet.extended_entities.keys():

            for m, media in enumerate(tweet.extended_entities["media"]):

                media_url = media["media_url"]
                media_file = requests.get(media_url)
                ext = media_url.split('.')[-1]

                file_name = str(tweet_id) + '_' + str(m) + '.' + ext

                with open(file_name , 'wb') as dl_file:
                    dl_file.write(media_file.content)
