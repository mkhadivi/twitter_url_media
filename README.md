# Twitter media downloader 
> Tweet media downloader (link support)

Download and save tweets with URL using twitter API.

In collecting Data from Twitter, especially media, the problem is that some tweets are shared using URLs, and we need to have the media of these tweets. By parsing this URL and using tags, this code saves that media. Currently, it is using the metadata of the site, the two tags 'twitter:image:src' and 'og:image'; in the future, I will try to add non-meta tags.

Unfortunately, you will not be able to download more than 3200 tweets.

Support media download on Twitter:
* Image - Get the URL and save.

## Requirements
```
 requests
 tweepy
 BeautifulSoup
```

## Get Twitter API keys
Since the code needs to access Twitter's APIs, API keys are necessary. You can use this [link](https://developer.twitter.com/en/docs/twitter-api).

Replace the following with your own API keys.

```
# twitter API 
CONSUMER_KEY = #ENTER_YOUR_CONSUMER_KEY
CONSUMER_SECRET = #ENTER_YOUR_CONSUMER_TOKEN
ACCESS_KEY = #ENTER_YOUR_ACCESS_KEY
ACCESS_SECRET = #ENTER_YOUR_ACCESS_TOKEN
```
## Arguments
* `tweet_id`: the tweet ID

## Usage
1. Download the script
2. Get tweet id
3. Run `main.py`

## Examples:
* provide tweet which contains url media, like: https://twitter.com/bbchealth/status/1552396076828737536

* get tweet_id: 1552396076828737536

* request url like: https://bbc.in/3zylMCZ
  
* download using:
```
python main.py 1552396076828737536
```

## Compatibility

Tested on Python 3.7 and above on Linux and Windows. Feel free to open an issue if you have bug reports, questions or any suggestions. If you want to collaborate, you're welcome.

## Todo

* ~~download Meta tag other than 'twitter:image:src'~~
* download images other than Meta tags