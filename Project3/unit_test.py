# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:39:48 2021

@author: 16418

These are tests of media_analyzer.py
"""

import media_analyzer as ma
import time
import helper as hp

def test_API_credentials():
    hp.console_print('testing the API credential status')
    api = ma.API_credentials()
    try:
        if api:
            hp.console_print('the API credential succeed')
    except:
        hp.console_print('the API credential failed')
        
    
def test_runtime():
    hp.console_print('testing the running time of the process')
    start = time.clock()
    ma()
    # input halloween
    end = time.clock()
    print('running time: %s seconds' %(end - start))
    
    
def test_wrong_input():
    hp.console_print('test the result of inputing a punctuation')
    ma.API_credentials()
    # input '!'
    result = ma.twitter_search()
    if len(result):
       hp.console_print('the twitter API has output')
    else:
        hp.console_print('the twitter API does not output')
    
    
def test_input_sentence():
    ma.API_credentials()
    # input 'a sentence'
    result = ma.twitter_search()
    if len(result):
       hp.console_print('the twitter API has output')
    else:
        hp.console_print('the twitter API does not output')
    
def test_tweets_num():
    hp.console_print('testing the number of tweets searched')
    ma.API_credentials()
    result = ma.twitter_search()
    if result == ma.twitter_search.total_tweets:
        print('the tweets number is correct')
    else:
        print('the numbes is not correct')
