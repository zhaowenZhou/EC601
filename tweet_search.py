# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:00:09 2021
This is used to search tweets.
@author: 16418
"""
import tweepy
import json

#Twitter API credentials
consumer_key = "UPPfRTTzJeQmN2qMMy5u4vcsx"
consumer_secret = "cXDdeBrOAa4eK4dQRKqa2EtCXuBO6ZO6zvF2k6LdfRbP4QBrt7 "
access_token = "1440734978036289550-F05e2EvrafilQzCqEK8yT9GjfT5MyU"
access_token_secret = "yqNGkN9dyJGWxoy6uGAEtUfRWJJuXDukg3nEKx4MhEBCJ"

# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#twitter search
search_words = input('please input the word you want to seatch')
searched_tweets = []
try:
    tweets = api.search(q = search_words, count = 10)
    if not tweets:
        print('no tweets found')
    searched_tweets.extend(tweets)
except tweepy.TweepError:
    print('exception raised')

numtweets = len(searched_tweets)
print('the number of tweets found is',numtweets)
if searched_tweets:
    file = open('tweet_search.json', 'w')
    for tweet in searched_tweets:
        json.dump(tweet._json, file, sort_keys = True, indent = 4)
        file.close()


