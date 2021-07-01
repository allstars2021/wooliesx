Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
import tweepy as tw
import pandas as pw
import json
consumer_key = 'S8E7F4LQ3uQkdBx48HisSL4ox'
consumer_secret = 'WueeKgFeIcXZkvSEL6a3Uwm1CscNljNbBw0p9k92alVBzTM7eO'
access_token = '1407989759071326209-NT8BIkl0XpFGRajHiVlNzFUQdB9I5N'
access_token_secret = 'qDpUZwmNQLoSudPG7zxlNjdYxGXRmMB99dwwrCcObxgS9'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)
import twitter
search_words = ("improve" or "food" or "movie" or "want to go")
date_since = "2021-06-26"
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
tweets
for tweet in tweets:
    print(tweet.text)
    
import csv
import sys
import config
from langdetect import detect
api.trends_available()[0]
{'name': 'Worldwide', 'placeType': {'code': 19, 'name': 'Supername'}, 'url': 'http://where.yahooapis.com/v1/place/1', 'parentid': 0, 'country': '', 'woeid': 1, 'countryCode': None}
for val in api.trends_available():
    if val['country'] == 'Australia':
        print(val.values())
        
def get_woeid(place):
    '''Get woeid by location'''
    try:
        trends = api.trends_available()
        for val in trends:
            if (val['name'].lower() == place.lower()):
                return(val['woeid']) 
        print('Location Not Found')
    except Exception as e:
        print('Exception:',e)
        return(0)

x = get_woeid('Australia')
def get_trends_by_location(loc_id,count):
    '''Get Trending Tweets by Location'''
    import iso639
    try:
        trends = api.trends_place(loc_id)
        df = pd.DataFrame([trending['name'],  trending['tweet_volume'], iso639.to_name(detect(trending['name']))] for trending in trends[0]['trends'])
        df.columns = ['Trends','Volume','Language']
        #df = df.sort_values('Volume', ascending = False)
        return(df[:count])
    except Exception as e:
        print("An exception occurred",e)

df_Australia_trends = get_trends_by_location(x,20)
df_Australia_trends

number_of_tweets = 50
username = []
tweets = []
likes = []
time = []
retweets = []
cursor = tw.Cursor(api.search, q = ("(foodie OR travel OR movie OR healthliving OR food AND (visit OR excited OR obsessed OR try OR love)) -filter: retweets lang:en"), tweet_mode = "extended").items(number_of_tweets)
for tweet in cursor:
    username.append(tweet.user.screen_name)
    tweets.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)
    retweets.append(tweet.retweet_count)

    
df = pd.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    df = pd.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})
NameError: name 'pd' is not defined
df = pw.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})
df
