import praw
import pprint
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import asyncio
from datetime import datetime
import time
import os

## How to use token to access your reddit
## Please get a token using :
##   python reddit.refresh.token.py
##
## Input * to the cmd line to define all scopes 
##
## Save the token from the output and save it to bash env variable REDDIT_TOKEN by:
##   export REDDIT_TOKEN="your_saved_token"
##
## Save webhook of discord to bash env variable DISCORD_REDDIT_WEBHOOK by:
##   export DISCORD_REDDIT_WEBHOOK="your_webhook"
## 
## Specify refresh_token in praw.Reddit bellow

## How to use password and username to accress your reddit
## Please specify password and username in praw.Reddit bellow

reddit = praw.Reddit(
    client_id="fE-qK2c4_Ms2gO-K7KvoVA",
    client_secret="hOLKBStyqGcT7dVo1Uzz1mfRL63ABg",
    refresh_token=os.environ['REDDIT_TOKEN'],
    #password="xxxx",
    user_agent="User-Agent: testscript by u/mypython",
    #username="xxx",
    check_for_async=False
)

print(reddit.user.me())


webhook_address = os.environ['DISCORD_REDDIT_WEBHOOK']


async def foo(reddit,webhook_address):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_address, adapter=AsyncWebhookAdapter(session))
        subreddit = reddit.subreddit("invites+OpenSignups")
        # assume you have a Subreddit instance bound to variable `subreddit`

        while true:
            try:
                for submission in subreddit.stream.submissions(skip_existing=True, pause_after = 0):
                    if(submission is None):
                        now = time.time()
                        print(datetime.fromtimestamp(now))
                        time.sleep(60)
                    else:
                        now = time.time()
                        age = now - submission.created_utc
                        await webhook.send("Date: " + str(datetime.fromtimestamp(submission.created_utc)) + "  URL: " + selfubmission.url)
            except Except as e:
                await asyncio.sleep(60)
                
asyncio.run(foo(reddit,webhook_address))




#     # assume you have a Subreddit instance bound to variable
#     print(submission.title)
#     # Output: the submission's title
#     print(submission.score)
#     # Output: the submission's score
#     print(submission.id)
#     # Output: the submission's ID
#     print(submission.url)
#     # Output: the URL the submission points to or the submission's URL if it's a self post
#     #pprint.pprint(vars(submission)



