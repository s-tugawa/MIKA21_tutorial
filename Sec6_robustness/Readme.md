# ネットワークのロバスト性解析
## Usage
次数順、ランダム、HDA (high degree adaptive) に従ってノードを削除した時の最大連結成分のサイズを求めるには、以下のようにプログラムを実行します。

ランダム
```bash
python3 random_remove.py network/ba.txt
```
次数順
```bash
python3 degree_remove.py network/ba.txt
```
HDA
```bash
python3 hda_remove.py network/ba.txt
```

チュートリアルテキスト内で用いたインターネットのルータレベルトポロジのデータは以下からダウンロードできます。
http://networksciencebook.com/translations/en/resources/data.html

## 練習問題
様々なネットワークの次数順攻撃やランダムノード削除に対するロバスト性を評価してみよう。
どのような構造的特徴を持つネットワークのロバスト性が高いか考察してみよう。
- http://snap.stanford.edu/data/index.html
- http://networksciencebook.com/translations/en/resources/data.html
