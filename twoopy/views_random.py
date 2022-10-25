from distutils.log import error
from inspect import getcomments
from django.shortcuts import render

import tweepy
import time
from django.http import HttpResponse, JsonResponse
import json
import time
import numpy as np

# consumer_key = 'dMLnu9OEmYM4hEOiHSXwqVqsE'
# consumer_secret = 'Z8gLC9koWLId5JSWwz5KWsENLl4XDn9PDtg6iKii4Pq5ZPeNI5'
# key = '891152839287881728-5c6c13DePo0tS0rYCYmv1zWYNk6aBJa'
# secret = 'BuhHmD0sZKaExLbi9p8YAgn20i1CAJpCIy4zAnUyPcKSX'

# consumer_key = 'Y44Yjx3Ubh5PxzMZJLr5UziKh'
# consumer_secret = 'CrjvptLWSHLme8CQl6y8jOKW6h33QZzoJOETsnJz6lulwpCDL5'
# key = '1538547199167959041-xDoFIwucZRsOFaxQwBFv3yPYnS8i1Z'
# secret = '8EsKmOrcgpxofAliTk0WRbRvq22s19jqgKQoz7WqOVuY3'

consumer_key = '7iGt2N5sgc0NnSW3veidjq1fd'
consumer_secret = '4AakFAGrcbOB3bmly7H8rwFSLkl3fc6jMp8NWVrMzMxFdOnIYO'
key = '1538547199167959041-gYvOryOzxb6u8ntA16Yjdmg0cpgoFW'
secret = 'qkVZHCzysa0TH2TUv1dJSdjgjIrBLHA5VqpQKY7V1AiUU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

contexts = []
greeting = [
    "こんにちは!\n\n",
    "こんにちは!MetaElfLand日本テレグラム管理人のケントです。\n\n",
    "こんにちは!MetaElfLand日本語テレグラム管理人をしています。\n\n",
    "初めまして、ケントです。\n\n",
    "こんにちは!初めまして、kentです。\n\n",
    "突然のリプ失礼します。\n\n",
    "初リプ失礼します。ケントです。\n\n",
    "突然のリプライ失礼します。\n\n",
    "FF外から失礼します。\n\n",
    "検索から失礼します。\n\n",
]

c1 = "MetaElfLandJapanボランティアを募集しています!\n❣️P2Eゲームに興味のある方\n❣️前向きポジティブな方https://t.me/MetaElfLandJapan さらに詳しく!\n\n"

c2 = "日本語テレグラムにてボランティアやってますので、ぜひ遊びに来てください。\nhttps://t.me/MetaElfLandJapan\n\n"

c3 = "NFTゲームを初めてみたいなって思う方へMetaElfLandについてご紹介したいと思います。\nもし興味があれば、私のプロフィールから詳しい情報をご入手ください。\n\n"

c4 = "新しいP2E型のNFTゲームMetaElfLandがもうすぐローンチされるのですが、もし気になるなら下のリンクから詳しい情報をご入手ください。\n\nテレグラム\nhttps://t.me/MetaElfLandJapan\n\n"

c5 = "日本市場へ!MetaElfLandJapan運用側のボランティアを募集しています。\nP2Eゲーム興味のある方はお気かるにご連絡ください。\n\nテレグラム\nhttps://t.me/MetaElfLandJapan\n\n"

c6 = "MetaElfLand(P2Eゲーム)の日本テレグラムのボランティアしてみませんか？\nhttps://t.me/MetaElfLandJapan\n\n"

c7 = "新しいP2EゲームMetaElfLandの特徴や機能の最新情報に発信していますので、よかったら私のプロフィールをご覧ください。\n\n"

c8 = "MetaElfLandの最新情報はSNSにて情報発信中です。\n詳しくはプロフィールまで。よろしく願いします。\n\n"

c9 = "ゲームをしながら稼ぐことも出来ますよ。\nぜひMetaElfLand(P2Eゲーム)をご注目ください。\n\n"

c10 = "今月の注目タイトルを紹介したいと思います。\nMetaElfLand!日本市場へ!\nもし興味があれば、私のツイッタから詳細をご入手ください。\n\n"

c11 = "マカオのMeta Soft社が開発しているP2EゲームMetaElfLandの特徴をテレグラム上で発信しています。\nhttps://t.me/MetaElfLandJapan さらに詳しく!\n\n"

c12 = "この度、マカオのMeta Soft社が開発しているP2EゲームMetaElfLandを紹介したいと思います。\nもしゲームに興味があれば、私のツイッタから詳細をご入手ください。\n\n"
content = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]

ending = [
    "決してスパムではありません。ご安心ください。\n\n",
    "変な案件ではありません。ご安心を。\n\n",
    "決して怪しいプロジェクトではありません。ご安心してご確認ください。\n\n",
    "決して怪しい者じゃありません。ご安心ください。\n\n",
    "日本語テレグラムにてボランティアやってます。ご安心をお願いします。\n\n",
    "決して怪しい話ではありません。プロジェクトの詳細をご確認の上ご判断ください。\n\n",
    "マカオのMetaSoft社が開発しているゲームですので、ご安心下さい。\n\n",
    "開発:MetaSoft(マカオ)\n\n",
]

tag = [
    "#P2Eゲーム",
    "#NFTゲーム",
    "#Play to Earn",
    "#稼げるNFTゲーム",
    "#ブロックチェーンゲーム",
    "#PvP",
    "#PvE",
    "#Player vs Player",
    "#Player vs Enemy",
    "#MELT",
    "#Mエルフコイン",
    "#仮想通貨",
    "#オンライン対戦ゲーム",
    "#オンラインゲーム",
    "#稼げるゲーム",
    "#稼げるNFTゲーム",
    "#MetaElfLand",
    "#MetaElfLandJapan",
    "#メタエルフランド",
    "#BattleNet Coin",
    "#BNC",
]
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
    # comment = request.POST.get('comment')
    ids = json.loads(ids)
    for item in ids:
        comment = getComment()
        sleepSecond = getSleepSecond()
        print("sleep %s seconds" % (sleepSecond[0]))
        time.sleep(sleepSecond[0])
        print("wait after %s seconds" % (sleepSecond[0]))
        reply_status = "@%s %s" % (item["user"].strip(), comment)
        try:
            response = api.update_status(status=reply_status, in_reply_to_status_id=item["id"])  
        except tweepy.error.TweepError as e:
            print(comment)
            print(e)
        print(comment)
        print(item["user"].strip())

    d = {
        'ids': ids,
    }
    print("finished")
    return JsonResponse(d)

def getSelectedGreeting():
    return np.random.choice(greeting, 1, p=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

def getSelectedContent():
    return np.random.choice(content, 1, p=[0.085,0.085,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083,0.083])

def getSelectedEnding():
    return np.random.choice(ending, 1, p=[0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125])

def getSelectedTag():
    tagCount = np.random.choice([1,2,3,4], 1, p=[0.1,0.3,0.4,0.2])
    return np.random.choice(tag, tagCount[0], p=[0.0535,0.0535,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047,0.047])

def getComment():
    selectedGreeting = getSelectedGreeting()
    selectedContent = getSelectedContent()
    selectedEnding = getSelectedEnding()
    selectedTag = getSelectedTag()
    comment = "%s %s %s %s" % (selectedGreeting[0], selectedContent[0], selectedEnding[0], selectedTag[0])
    return comment

def getSleepSecond():
    return np.random.choice([6,31,117,220,560,732], 1, p=[0.1,0.1,0.1,0.3,0.3,0.1])
