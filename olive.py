import tweepy
import time

consumer_key = 'S8E7F4LQ3uQkdBx48HisSL4ox'
consumer_secret = 'WueeKgFeIcXZkvSEL6a3Uwm1CscNljNbBw0p9k92alVBzTM7eO'

key ='1407989759071326209-NT8BIkl0XpFGRajHiVlNzFUQdB9I5N'
secret = 'qDpUZwmNQLoSudPG7zxlNjdYxGXRmMB99dwwrCcObxgS9'

#ACCESS_TOKEN = key, ACCESS_TOKEN_SECRET = secret, 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

#tweets = api.mentions_timeline()

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '@allstars_2021' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("Dear " + "@" + tweet.user.screen_name + ", We are sorry to hear this. A member from our team will get back to you and please visit https://www.woolworths.com.au/shop/page/help-and-support-faq in the meantime and see if our digital member Olive can help you out.", tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True: 
    reply()
    time.sleep(10)