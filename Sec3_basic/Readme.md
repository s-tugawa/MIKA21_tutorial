# 基本的な特徴量の計算
MIKA2021チュートリアルの3章で用いたコードです。
## Usage
9章で用いた MIKA 関連研専のネットワークの特徴量を計算するには、以下のように実行します。
```bash
python3 calc_feature.py MIKA_net.txt
```
MIKA_net.txt の部分を分析したいネットワークのエッジリストに置き換えると、そのネットワークの特徴量が計算できます。  
エッジリストはタブ区切りであることを前提にしていますが、ソースコードの以下の部分
```python
G=nx.read_edgelist(file,nodetype=str,encoding='utf-8',delimiter="\t")
```
のdelimieterを書き換えれば任意の区切り文字のエッジリストを読み込むことができます。

## 練習問題
以下のページからネットワークのデータをダウンロードして特徴量を計算してみましょう。
- http://snap.stanford.edu/data/index.html
- http://networksciencebook.com/translations/en/resources/data.html
