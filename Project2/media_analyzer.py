# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 09:13:18 2021
# tweet search and google nlp analysis
@author: 16418
"""
import tweepy

from google.cloud import language_v1
from datetime import datetime, timedelta



#Twitter API credentials
def API_credentials():
    consumer_key = input('please input consumen key')
    consumer_secret = input('please input consumen secret')
    access_token = input('please input access token')
    access_token_secret = input('please input your access token secret')
    
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


# twitter search
def twitter_search():
    num = int(input('please input the expected tweets neumber'))
    searchword = input('type in the word you want to search')
    api = API_credentials()
    total_tweets = num
    search_words = str(searchword)
    today_datetime = datetime.today().now()
    searchsince_datetime = today_datetime - timedelta(days = 5)
    searchsince_date = searchsince_datetime.strftime('%Y-%m-%d') 
    searched_tweets = tweepy.Cursor(api.search, q = search_words, 
                                    since = searchsince_date, 
                                    result_type = 'recent', 
                                    lang = 'es').items(total_tweets)
    return(searched_tweets)

# authorize google cloud
def authorize_google():
    searched_tweets = twitter_search()
    language_client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=searched_tweets, type_=language_v1.Document.Type.PLAIN_TEXT)
    SENTI_RESULT = language_client.analyze_sentiment(request={'document': document}).document_sentiment.score
    
    print("SentimentResult: {}".format(SENTI_RESULT))
   
    
if __name__ == '__main__':
    API_credentials()
    twitter_search()
    authorize_google()