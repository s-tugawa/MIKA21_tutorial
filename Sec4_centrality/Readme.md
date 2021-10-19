# 中心性解析
## Usage
あるネットワークの各ノードの中心性指標を計算するには以下のようにプログラムを実行します。
```bash
python3 calc_centrality.py high_tech/advice.txt
```
チュートリアル資料中にある論文の共著関係ネットワークの中心性と論文の被引用数の関係を求めるには、以下のようにプログラムを実行します。
```bash
python3 calc_cent_citation.py aps/apscoauthor.csv aps/citation_count.txt >result.txt
```
ペアプロットは、以下のようにプログラムを実行すると、pairplot.eps という名前でファイルが出力されます。かなり点数が多いので、時間がかかるのに注意。
```bash
python3 pair_plot.py result.txt
```

## 練習問題
以下のページからネットワークのデータをダウンロードして中心性を計算してみましょう。
中心性指標によってノードのランキングがどのように異なるか考察してみましょう。
- http://snap.stanford.edu/data/index.html
- http://networksciencebook.com/translations/en/resources/data.html
