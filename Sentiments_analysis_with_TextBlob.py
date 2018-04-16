
# coding: utf-8

# In[3]:


### A small code for sentiment analysis on tweets using TextBlob library
### Using Tweepy to extract the tweets
import tweepy  
from textblob import TextBlob

consumer_key = 'xpcvfDaZvTAZXsBi7r9ziAtsE' # enter your cosumer key from twitter 
consumer_secret = '8qxVuGF56qvDAbRKQ6ZZggms39CElptK8muca62YUYDactEENS'  # enter your cosumer key from twitter
access_token = '561845343-dnHHnsoFWHLNatlshJeTbwsEdQHBiqziN2mW8dNl'   # enter your access token from twitter
access_token_secret = 'GnV44K5wDeAb4YycizTVYo2H41EFlJxoANwE1tpFxaYKI'  # enter your access token secret from twitter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)   # using OAuthHandler method for autherization 
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
tweets = api.search('victim of kathua')  # Searching all the tweets related to a topic

# looping throuth the tweets and printing the tweets with the sentiment analysis.
for i in tweets:  
    print(i.text)   
    analysis = TextBlob(i.text)
    print(analysis.sentiment)


# In[ ]:




