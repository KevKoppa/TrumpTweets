import tweepy

# Twitter authorization keys declared
CONSUMER_KEY = "MpaHD8Njtwld5vIRuP9kYL9VU"
CONSUMER_SECRET = "kO0NswJljNE5Jbav5bQD8Bo0T60UTkV8bMLwlmDapCrNc7DAgE"
TWITTER_KEY = "1191156315273486337-1QVNvcsORxTaBPJNp19pML42ryDLex"
TWITTER_SECRET = "kFR7gm2OZdvSguYjXlnnLSrvj8iqJZiwMFxInMkIW5SVx"

# Authorization to use Twitter's API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)

# Define the search term and the date_since date as variables
search_words = "trump" + "-filter:retweets"
date_since = "2020-10-03"

# Collect tweets
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(100)

list = []
LIMIT = 10
for tweet in tweets:
    if (not(tweet.truncated) and len(list) <= LIMIT):
        list.append(tweet.text)

print(list)
