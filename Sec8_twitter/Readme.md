# Twitter のエゴネットワーク解析
## Usage
まず、get_followers.py および get_friends.py の冒頭部分に API にアクセスするための key の情報を入力する。
次に作業用ディレクトリに followers および following という名前のディレクトリを作成する。
```bash
mkdir followers
mkdir following
```
hoge というユーザ名のフォロワーを取得する際には、以下のようにプログラムを実行する。
```bash
python3 get_followers.py hoge
```
これで、followers/hoge.txt にhogeのフォロワーリストが出力される。
さらに hoge のフォロワーのフォロイーのリストを取得するには以下のようにする。
```bash
sh crawl.sh followers/hoge.txt
```
これで、各フォロワーのフォロイーのリストが following/XX.txt に保存される。
hoge のエゴネットワークを構築するには、以下のようにプログラムを実行する。
```bash
python3 make_egonet.py followers/hoge.txt
```

## Requirements
フォロワー (フォロイー) 取得には tweepy というモジュルールが必要です。pip でインストールしてください。
```bash
pip3 install tweepy
```
