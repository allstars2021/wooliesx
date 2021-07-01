#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import tweepy as tw
import pandas as pd
import json


# In[2]:


consumer_key = 'S8E7F4LQ3uQkdBx48HisSL4ox'


# In[3]:


consumer_secret = 'WueeKgFeIcXZkvSEL6a3Uwm1CscNljNbBw0p9k92alVBzTM7eO'
access_token = '1407989759071326209-NT8BIkl0XpFGRajHiVlNzFUQdB9I5N'
access_token_secret = 'qDpUZwmNQLoSudPG7zxlNjdYxGXRmMB99dwwrCcObxgS9'


# In[4]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)
import twitter


# In[5]:


search_words = ("improve" or "food" or "movie" or "want to go")


# In[6]:


date_since = "2021-06-26"


# In[7]:


tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(10)


# In[8]:


for tweet in tweets:
    print(tweet.text)


# In[9]:


import csv
import sys
import config


# In[10]:


from langdetect import detect


# In[11]:


api.trends_available()[0]


# In[23]:


for val in api.trends_available():
    if val['country'] == 'Australia':
        print(val.values())


# In[13]:


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


# In[14]:


x = get_woeid('Australia')


# In[15]:


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


# In[16]:


df_Australia_trends = get_trends_by_location(x,20)


# In[17]:


df_Australia_trends


# In[18]:


number_of_tweets = 50 
username = []
tweets = []
likes = []
time = []
retweets = []


# In[19]:


cursor = tw.Cursor(api.search, q = ("(foodie OR travel OR movie OR healthliving OR food AND (visit OR excited OR obsessed OR try OR love)) -filter: retweets lang:en"), tweet_mode = "extended").items(number_of_tweets)


# In[20]:


for tweet in cursor:
    username.append(tweet.user.screen_name)
    tweets.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)
    retweets.append(tweet.retweet_count)


# In[21]:


df = pd.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})


# In[22]:


df


# In[ ]:




