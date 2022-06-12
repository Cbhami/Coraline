# tweetutilities.py
"""Utility functions for interacting with Tweepy objects."""
from geopy import OpenMapQuest
from textblob import TextBlob 
import os
import time 
import tweepy

def get_tweepy_API(wait=True, notify=True):
    """Authenticate with Twitter and return API object."""
    # configure the OAuthHandler
    auth = tweepy.OAuthHandler(os.environ['APIK'],
                               os.environ['APISK']) #Set up the app keys
    auth.set_access_token(os.environ['ACCTO'],
                          os.environ['ACCTOS']) #set up your user tokens
    # get the API object
    return tweepy.API(auth, wait_on_rate_limit=wait, 
                      wait_on_rate_limit_notify=notify)

def print_tweets(tweets):
    """For each Tweepy Status object in tweets, display the 
    user's screen_name and tweet text. If the language is not
    English, translate the text with TextBlob."""
    for tweet in tweets:
        print(f'{tweet.user.screen_name}:', end=' ')
    
        if 'en' in tweet.lang:
            print(f'{tweet.text}\n')
        elif 'und' not in tweet.lang:  # translate to English first
            print(f'\n  ORIGINAL: {tweet.text}')
            try:
                print(f'TRANSLATED: {TextBlob(tweet.text).translate()}\n')
            except:
                print('Unable to translate tweet')

def get_tweet_content(tweet, location=False):
    """Return dictionary with data from tweet (a Status object)."""
    fields = {}
    fields['screen_name'] = tweet.user.screen_name

    # get the tweet's text
    try:  
        fields['text'] = tweet.extended_tweet.full_text
    except: 
        fields['text'] = tweet.text

    if location:
        fields['location'] = tweet.user.location

    return fields

def get_geocodes(tweet_list):
    """Get the latitude and longitude for each tweet's location.
    Returns the number of tweets with invalid location data."""
    print('Getting coordinates for tweet locations...')
    geo = OpenMapQuest(api_key=os.environ['GeoCK'])  # geocoder
    bad_locations = 0  

    for tweet in tweet_list:
        processed = False
        delay = .1  # used if OpenMapQuest times out to delay next call
        while not processed:
            try:  # get coordinates for tweet['location']
                geo_location = geo.geocode(tweet['location'])
                processed = True
            except:  # timed out, so wait before trying again
                print('OpenMapQuest service timed out. Waiting.')
                time.sleep(delay)
                delay += .1

        if geo_location:  
            tweet['latitude'] = geo_location.latitude
            tweet['longitude'] = geo_location.longitude
        else:  
            bad_locations += 1  # tweet['location'] was invalid
    
    print('Done geocoding')
    return bad_locations