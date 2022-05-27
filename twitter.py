import tweepy
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import os
import yaml
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAAmAYgEAAAAAOUySvg6BlCkxbQJeayj1BkF0%2BbM%3Do7E91H0PyAQYqSFrd648xTeomRujHFOi33a4Ua6neNhOuMWPwg")

## auth = tweepy.OAuth2AppHandler(
##      "G05moHo52i0r1QCzsfkQBN5Yp", "RtQHF2RdTacVNiKlnLpFrJM1V90kfk2izdZWQHqYnUFhLtq9YN"
#     )
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#         print(tweet.text)
allfriend=[]

for friend in api.get_user(screen_name="crnormal").friends():
    allfriend = allfriend + [friend.id_str]

##print(allfriend)

async def send2Webhook(status):
    async with aiohttp.ClientSession() as session:
        webhook_address = os.environ['DISCORD_TWITTER_WEBHOOK']
        webhook = Webhook.from_url(webhook_address, adapter=AsyncWebhookAdapter(session))
        await webhook.send(status.text)



class Listener(tweepy.Stream):
    # def __init__(self, output_file=sys.stdout):
    #     super(Listener,self).__init__()
    #     self.output_file = output_file
    def on_status(self, status):
        asyncio.run(send2Webhook(status))
    def on_error(self, status_code):
        print(status_code)
        return False


listener = Listener(
    consumer_key="G05moHo52i0r1QCzsfkQBN5Yp",
    consumer_secret="RtQHF2RdTacVNiKlnLpFrJM1V90kfk2izdZWQHqYnUFhLtq9YN",
    access_token =     "3289316244-ES3AnHb6bK2IoHE8le3cNcZxEy5ynwl4VEPw890",
    access_token_secret =     "AZvYrSJHYIpDuvoPIDJUJU4MvVtGKbQKnUwEKrBxymUl4"
)

listener.filter(follow=allfriend)
