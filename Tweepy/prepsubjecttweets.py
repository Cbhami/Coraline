import tweepy
import os
import preprocessor as p #Note: if no options are set ALL will be used in cleaning
from pdb import set_trace


APIK = 'F9Ke5EmViAHKPWFAvxNw5WEjr'
APISK = 'pqoItDgEXYUji6SnSmAAaLeTQuIHH0VVCUyDZaUUdhJpgkkmUS'
ACCTO = '2777419660-hIblVunw1TwIbGqiNE9HWcogMx3OaxTtRe0YxJN'
ACCTOS = 'nB1BvZou1sC6v4ElFYrFrUrRxMtvmLWvaXjrb9S82ajX8'
GeoCK = 'Xjd7GQpnGFWaslP9o9KTVecDi6KmlSq7'

os.environ['APIK']=APIK
os.environ['APISK']=APISK
os.environ['ACCTO']=ACCTO
os.environ['ACCTOS']=ACCTOS
os.environ['GeoCK']=GeoCK

def prepsubject(subject,quantity):
    auth = tweepy.OAuthHandler(APIK,
                               APISK) #Set up the app keys
    auth.set_access_token(ACCTO,
                          ACCTOS) #set up your user tokens
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True) #ALWAYS use wait_on_rate_limit to prevent yourself from getting blocked
    
    tweets = api.search(q=subject+' lang:en', count=quantity) #insure only English-language tweets returned
    tweet_text_raw = [] #store raw and preprocessed tweets in separate lists
    tweet_text_prep = []
    for tweet in tweets:
        tweet_text_raw.append(tweet.text)
        tweet_text_prep.append(p.clean(tweet.text))
    
    return tweet_text_raw,tweet_text_prep