from distutils.log import error
from inspect import getcomments
from django.shortcuts import render

import tweepy
import time
from django.http import HttpResponse, JsonResponse
import json
import time
import numpy as np

# your developer twitter consumer key
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# your developer twitter consumer secret
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# your developer twitter access key
access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# your developer twitter access secret
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

contexts = []

def top(request):
    keyword = request.GET.get('keyword');
    contexts.clear()
    if keyword:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword).items(10):
            contexts.append({
                'id': tweet.id_str,
                'user': tweet.user.screen_name,
                'text': tweet.text,
                'follower': tweet.user.followers_count,
                'date': tweet.created_at,
                'favourite': tweet.user.favourites_count,
            })
            print(tweet)

    return render(request, "top/index.html", {'contexts':contexts, 'keyword':keyword})


def reply(request):
    ids = request.POST.get('ids')
    comment = request.POST.get('comment')
    ids = json.loads(ids)
    for item in ids:
        sleepSecond = getSleepSecond()
        print("sleep %s seconds" % (sleepSecond[0]))
        #time.sleep(sleepSecond[0])
        time.sleep(1)
        print("wait after %s seconds" % (sleepSecond[0]))
        reply_status = "@%s %s" % (item["user"].strip(), comment)
        try:
            response = api.update_status(status=reply_status, in_reply_to_status_id=item["id"])  
        except tweepy.errors.TweepyException as e:
            print(comment)
            print(e)
        print(comment)
        print(item["user"].strip())

    d = {
        'ids': ids,
    }
    print("finished")
    return JsonResponse(d)

def getSleepSecond():
    return np.random.choice([6,31,117,220,560,732], 1, p=[0.1,0.1,0.1,0.3,0.3,0.1])
