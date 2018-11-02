import tweepy
import time
import sys
from datetime import datetime
from time import sleep

CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_SECRET=""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

userid = "hideki_climax"

followers_id = api.followers_ids(userid)
#自分のアカウントのフォロワーをすべて取得する

following_id = api.friends_ids(userid)
#自分のアカウントのフォロイングをすべて取得する

for following in following_id: #自分がフォローしているユーザーだけ取得する
  
    if following not in followers_id: #自分のフォローしているユーザーで、フォロワーに属さないユーザーを取得する　
      
        userfollowers = api.get_user(following).followers_count
        if userfollowers < 100:
            print("リムーブするユーザー名")
            username = api.get_user(following).name
            print(username)
            print("フォロワー数")
            print(userfollowers)
            api.destroy_friendship(following)
