import tweepy
from time import sleep

minute = 60

consumer_key = "ZMStQd7o698CXe1kbb9K7pmQN"
consumer_secret = "S6kzYrIREWCxnRX00erOHF4TWxbhNduBdlQbvj1al9EnuVqWAU"

access_token = "1363296206-OhazXflCmmRZgCdIv8nbHaE2XYiQbsWDwspNmgm"
access_token_secret = "YSvDkxc65e08cR2uFtjc19cl8tYWxNwN1LNjxk23XfBOH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_user_latest_tweet(username):
    user_tweets = api.user_timeline(username)
    if user_tweets:
        return user_tweets[0].text
    else:
        return None

def tweet(text):
    api.update_status(text)

def should_tweet(my_latest_tweets, famous_person_latest_tweet):
    if famous_person_latest_tweet in my_latest_tweets:
        return False
    else:
        return True

def clout_chase_tweet(famous_person):
    my_latest_tweets = api.user_timeline("connorwclancy")
    famous_person_latest_tweet = get_user_latest_tweet(famous_person)
    if should_tweet(my_latest_tweets, famous_person_latest_tweet):
        tweet(famous_person_latest_tweet)

def tweet_loop():
    famous_people = ["emmachamberlain"]
    for famous_person in famous_people:
        clout_chase_tweet(famous_person)


while True:
    tweet_loop()
    sleep(minute*5)


