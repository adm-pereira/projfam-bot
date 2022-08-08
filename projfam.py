import tweepy
import urllib.request
import schedule
import time

# Initialize

all_keys = open('ProjFamKeys', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
api_access_token = all_keys[2]
api_access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(api_access_token, api_access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

# Profile bio

bio = "Tweeto barras do Prof a cada 6 horas.\nPara receberes uma pic surpresa menciona @ProjFam6"
github = "https://github.com/adm-pereira/projfam-bot"
api.update_profile(description = bio, url = github)

# -------------------------------
# Constants


# -------------------------------

print("Started scheduling!")

def job():
    # select random tweet
    # api.update_status()
    print("something")

schedule.every(6).hours.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)


