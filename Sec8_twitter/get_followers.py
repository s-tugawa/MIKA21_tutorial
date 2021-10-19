import tweepy
import sys

# ここに自分のキーとトークンを入れる
consumer_key, consumer_secret = "", ""
access_token_key, access_token_secret = "", ""



name=str(sys.argv[1]) # Twitter アカウント名
path_follower="followers/"+name+".txt"#出力先

cursor = -1
with open(path_follower, mode='w') as f:
    while cursor != 0:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        itr = tweepy.Cursor(api.followers_ids, id=name, cursor=cursor).pages()
        try:
            for follower_id in itr.next():
                try:
                    print(follower_id)
                    f.write(str(follower_id)+'\n')
                except tweepy.error.TweepError as e:
                    print(e.reason)
        except ConnectionError as e:
            print(e.reason)
        cursor = itr.next_cursor

