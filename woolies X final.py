Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import tweepy as tw
im
>>> import pandas as pw
>>> import json
>>> consumer_key = 'S8E7F4LQ3uQkdBx48HisSL4ox'
>>> consumer_secret = 'WueeKgFeIcXZkvSEL6a3Uwm1CscNljNbBw0p9k92alVBzTM7eO'
>>> access_token = '1407989759071326209-NT8BIkl0XpFGRajHiVlNzFUQdB9I5N'
>>> access_token_secret = 'qDpUZwmNQLoSudPG7zxlNjdYxGXRmMB99dwwrCcObxgS9'
>>> auth = tw.OAuthHandler(consumer_key, consumer_secret)
>>> auth.set_access_token(access_token, access_token_secret)
>>> api = tw.API(auth,wait_on_rate_limit=True)
>>> import twitter
>>> search_words = ("improve" or "food" or "movie" or "want to go")
>>> date_since = "2021-06-26"
>>> tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
>>> tweets
<tweepy.cursor.ItemIterator object at 0x1150cea00>
>>> for tweet in tweets:
    print(tweet.text)

    
RT @foundmyfitness: A ketogenic diet may improve immunity and reduce excessive inflammation. 

Participants on a ketogenic diet for 3 weeks…
RT @LISANATIONS_: Please click the link, stay for 1 minute and send us screenshots! You dont need to log in. This to improve Lisa's search…
RT @ChrisWoodsMayor: I believe that the priorities of the city should be reflected in the budget. I reject the notion that the problems wit…
RT @wpninjasummit: Next interesting session: “Improve the reliability of ConfigMgr site with active/passive site servers” with Panu Saukko…
Weed can improve your #sexlife
>>> import csv
>>> import sys
>>> import config
>>> from langdetect import detect
>>> api.trends_available()[0]
{'name': 'Worldwide', 'placeType': {'code': 19, 'name': 'Supername'}, 'url': 'http://where.yahooapis.com/v1/place/1', 'parentid': 0, 'country': '', 'woeid': 1, 'countryCode': None}
>>> for val in api.trends_available():
    if val['country'] == 'Australia':
        print(val.values())

        
dict_values(['Perth', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1098081', 23424748, 'Australia', 1098081, 'AU'])
dict_values(['Adelaide', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1099805', 23424748, 'Australia', 1099805, 'AU'])
dict_values(['Brisbane', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1100661', 23424748, 'Australia', 1100661, 'AU'])
dict_values(['Canberra', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1100968', 23424748, 'Australia', 1100968, 'AU'])
dict_values(['Darwin', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1101597', 23424748, 'Australia', 1101597, 'AU'])
dict_values(['Melbourne', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1103816', 23424748, 'Australia', 1103816, 'AU'])
dict_values(['Sydney', {'code': 7, 'name': 'Town'}, 'http://where.yahooapis.com/v1/place/1105779', 23424748, 'Australia', 1105779, 'AU'])
dict_values(['Australia', {'code': 12, 'name': 'Country'}, 'http://where.yahooapis.com/v1/place/23424748', 1, 'Australia', 23424748, 'AU'])
>>> def get_woeid(place):
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

>>> x = get_woeid('Australia')
>>> def get_trends_by_location(loc_id,count):
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

        
>>> df_Australia_trends = get_trends_by_location(x,20)
An exception occurred name 'pd' is not defined
>>> df_Australia_trends
>>> number_of_tweets = 50
>>> username = []
>>> tweets = []
>>> likes = []
>>> time = []
>>> retweets = []
>>> cursor = tw.Cursor(api.search, q = ("(foodie OR travel OR movie OR healthliving OR food AND (visit OR excited OR obsessed OR try OR love)) -filter: retweets lang:en"), tweet_mode = "extended").items(number_of_tweets)
>>> for tweet in cursor:
    username.append(tweet.user.screen_name)
    tweets.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)
    retweets.append(tweet.retweet_count)

    
>>> df = pd.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    df = pd.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})
NameError: name 'pd' is not defined
>>> df = pw.DataFrame({'username':username, 'tweets':tweets, 'likes':likes, 'time':time, 'retweets':retweets})
>>> df
           username  ... retweets
0   kerokoidreturns  ...       18
1   bananafucknmilk  ...       18
2     kulugulutimes  ...       10
3      Swetha_Loves  ...       10
4          Gpriyaa1  ...       10
5         shriicuts  ...       10
6      _retweets___  ...      120
7    Love_Mamamoo12  ...       77
8            TyjahO  ...      100
9         colby_art  ...        2
10         smkfan99  ...        2
11         smkfan99  ...        2
12      wateryymoon  ...      106
13    Food_lover134  ...       45
14    WardOffDemons  ...        0
15      sapphicxsam  ...      106
16      willwouldnt  ...      106
17   muneca_muneca_  ...      106
18     kirbyparfait  ...      106
19    ocean_cracker  ...      106
20   KaraokeYamsElf  ...      106
21       SunnySokka  ...      106
22         pakukiss  ...      106
23        burntpaws  ...      106
24         bepo0005  ...      106
25     SlNlSTERSUNS  ...      106
26       MimiDotTee  ...      106
27   missmellohello  ...      106
28           REES0N  ...      106
29      snakechurch  ...      106
30   angelsucculent  ...      106
31         tepidtii  ...      106
32  nonbinarysinner  ...      106
33   MiracleRavioli  ...      106
34         Laney1_0  ...      106
35          fritula  ...      106
36      lesbiankory  ...      106
37      lanzhanIove  ...      106
38         sureinas  ...      106
39       belzzebbub  ...      106
40    HauntedPlague  ...      106
41      Moonscastle  ...      106
42   PlaguedDoctors  ...      106
43         wrthreeh  ...      106
44      cherrytusks  ...      106
45       cloudwifes  ...      106
46        sunsetven  ...      106
47          BATFLSH  ...      106
48    shinkulovebot  ...      106
49        shiginope  ...      106

[50 rows x 5 columns]
>>> df
           username  ... retweets
0   kerokoidreturns  ...       18
1   bananafucknmilk  ...       18
2     kulugulutimes  ...       10
3      Swetha_Loves  ...       10
4          Gpriyaa1  ...       10
5         shriicuts  ...       10
6      _retweets___  ...      120
7    Love_Mamamoo12  ...       77
8            TyjahO  ...      100
9         colby_art  ...        2
10         smkfan99  ...        2
11         smkfan99  ...        2
12      wateryymoon  ...      106
13    Food_lover134  ...       45
14    WardOffDemons  ...        0
15      sapphicxsam  ...      106
16      willwouldnt  ...      106
17   muneca_muneca_  ...      106
18     kirbyparfait  ...      106
19    ocean_cracker  ...      106
20   KaraokeYamsElf  ...      106
21       SunnySokka  ...      106
22         pakukiss  ...      106
23        burntpaws  ...      106
24         bepo0005  ...      106
25     SlNlSTERSUNS  ...      106
26       MimiDotTee  ...      106
27   missmellohello  ...      106
28           REES0N  ...      106
29      snakechurch  ...      106
30   angelsucculent  ...      106
31         tepidtii  ...      106
32  nonbinarysinner  ...      106
33   MiracleRavioli  ...      106
34         Laney1_0  ...      106
35          fritula  ...      106
36      lesbiankory  ...      106
37      lanzhanIove  ...      106
38         sureinas  ...      106
39       belzzebbub  ...      106
40    HauntedPlague  ...      106
41      Moonscastle  ...      106
42   PlaguedDoctors  ...      106
43         wrthreeh  ...      106
44      cherrytusks  ...      106
45       cloudwifes  ...      106
46        sunsetven  ...      106
47          BATFLSH  ...      106
48    shinkulovebot  ...      106
49        shiginope  ...      106

[50 rows x 5 columns]
>>> 