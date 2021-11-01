# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:00:09 2021
This is used to search tweets.
@author: 16418
"""
import tweepy
import json
import datetime as dt

#Twitter API credentials
def load_twitter_api():
    consumer_key = ""
    consumer_secret = " "
    access_token = ""
    access_token_secret = ""
    
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

#twitter search
def twitter_search(api, search_word, since_id, max_id, max_tweet_num):
    ''' q: searching words
        since_id, max_id: range(sin_id, max_id)
        max_tweet_num: the num of tweet searched
    '''
    searched_tweets = []
    while len(searched_tweets) < max_tweet_num:
        left_tweets = max_tweet_num - len(searched_tweets)
        try:
            new_tweets = api.search(q = search_word, count = left_tweets, 
                                    since_id = str(since_id), 
                                    max_id = str(max_id)
                                    )
            if not new_tweets:
                print('no content found')
                break
            searched_tweets.extend(new_tweets)
            max_id = searched_tweets[-1].id - 1
        except tweepy.TweepError:
            print('exception raised')
            break      
    return searched_tweets, max_id



def get_since_id(api, query, date = '', date_day = 5, ):
    # return the id of that day
    if date:
        td = date - dt.timedelta(days = date_day)
        format_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet_since = api.search(q = query, count = 10, until = format_date)
        return tweet_since[0].id
    # return the id of 5 days before today
    else:
        td = dt.datetime.now() - dt.timedelta(days = date_day)
        format_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet_since = api.search(q = query, count = 10, until = format_date)
        return tweet_since[0].id
    
    
def get_max_id(api, query, date = '', ):
    if date:
        td = date + dt.timedelta(days = 1)
        format_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet_max = api.search(q = query, count = 10, until = format_date)
        return tweet_max[0].id
    # return the id of 5 days before today
    else:
        td = dt.datetime.now() + dt.timedelta(days = 1)
        format_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet_max = api.search(q = query, count = 10, until = format_date)
        return tweet_max[0].id
    
    
def main():
    search_word = 'github'
    max_tweet_num = 50
    
    # get the api autorization and two ids
    api = load_twitter_api()
    since_id = get_since_id(api, query = search_word)
    max_id = get_max_id(api, query = search_word)
    
    # set parameters
    search_word = 'github'
    twitter, max_id = twitter_search(api, search_word, since_id, max_id, 
                                     max_tweet_num)
    
    
    # write a file to store tweets
    if twitter:
        file = open('tweet_search.json', 'w')
        for tweet in twitter:
            json.dump(tweet._json, file, sort_keys = True, indent = 4)
            file.close()
    else:
        print('no twitter found')
    
    
if __name__ == "__main__":
    main()
