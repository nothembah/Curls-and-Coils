import pip
import tweepy
import time

consumer_key = 'irx6itiPCo7thps6AV01gpk1s'
consumer_support = 'GXKwQb3DiLawoIldD3kSaApcanwM9EJaMVd1ZLJ6iC1X36sIUz'
access_key = '1416082513039183872-CBO6542jvo5Ypo7zNZlZwkisHpQfAw'
access_secret = 'MwRLJWj8EtdLu38Mnr2MXdTlGTIj039r9UUIqvwd3mn0f'

auth = tweepy.OAuthHandler(consumer_key, consumer_support)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()

search = 'naturalhair'
phrase = "Yaas! So good!"
num_of_tweets = 500

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:
        tweet.retweet()
        tweet.favorite()
        print('Retweet and Favorite')
        time.sleep(0)
    except tweepy.TweepError as e:
            print(e.reason)
    except StopIteration:
            break