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

#検索キーワード

while True:
    
    q = "" #ここに検索キーワードを設定
    count = 100

    search_results = api.search(q=q, count=count, lang="ja")

    for result in search_results:
        username = result.user._json['screen_name'] 
        tweet_id = result.id #Tweetのidを取得
        user_id = result.user._json['id'] #ユーザーのidを取得
        user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
        tweet = result.text #ツイートの内容を追加
        time = result.created_at #ツイートの日時を取得
        try:
            api.create_favorite(tweet_id) #favする
            print(user_id)
            print(user)
            print("をいいねしました")
            sleep(5)
            
            userfollowers = api.get_user(user_id).followers_count
            if api.exists_friendship(user_id, "自分のtwitterのID") == False:
                if userfollowers >200:
                    api.create_friendship(user_id) #フォローする
                    print(user)
                    print("をフォローしました")
                    sleep(5)

        except Exception as e:
            print(e)
            sleep(5)
    sleep(3600)