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

bio = "Tweeto barras do Prof a cada 6 horas.\nPara receberes uma pic surpresa menciona @ProjFam6\n---em desenvolvimento---"
github = "https://github.com/adm-pereira/projfam-bot"
api.update_profile(description = bio, url = github)

# Lyrics read

def read_lyrics_file():
    quote_count = 0

    lyrics_file = open('lyrics.txt', 'r', encoding='utf-8').read().splitlines()

    all_quotes = []

    quote = ""

    for line in lyrics_file:

        if line.startswith('-'):
            
            if quote != "":
                
                if len(quote) > 280:
                    print("----------" + str(len(quote)) + "/280 in\n")
                    print(quote)
                else:
                    all_quotes.append(quote)
            quote = ""
        else:
            quote = quote + line + "\n"

    return all_quotes


# Scheduling

print("Started scheduling!")

def job():
    # select random tweet
    # api.update_status()
    print("something")

schedule.every(6).hours.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)


