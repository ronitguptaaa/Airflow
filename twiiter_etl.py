import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "vqILreymZpzIyDgQhGnZPmkqh"
access_secret = "kgXuueljf04dM0U2jU8R2sDNMP7Hy3REOE0sPwYXRmCOkOGSWn"
consumer_key = "1704741479493648384-qqwj6IvJLsn8PkzXhNiIwu6f5b4YX4"
consumer_secret = "jfBNYXykqbOznzcKo4AdQRMpaqJheHgKWmS37yitUqbxG"

# Twitter Authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           count=200,
                           inculde_rts=False,
                           tweet_mode='extended'
                           )

tweet_list = []
for tweet in tweets:
    text = tweet._json["Full Text"]
    
    redefined_tweet = {"user":tweet.user.screen_name,
                       'text':text,
                       'favourite_count':tweet.favourite_count,
                       'retweet_count':tweet.retweet_count,
                       'created_at':tweet.created_at
    }
    tweet_list.append(redefined_tweet)
    

df = pd.DataFrame(tweet_list)
df.to_csv("elonmusk")