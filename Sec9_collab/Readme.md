# 研究者ネットワークの解析
## Usage
信学会の研究会システムから例えば CQ 研究会の2020年度の各発表の著者をlist.txtに出力するには、以下のようにプログラムを実行する。
```bash
python3 scraper.py 20 CQ >list.txt
```
list.txt の発表リストから共著ネットワークを構築するには以下のように実行する。
```bash
python3 construct_net.py list.txt
```
テキスト中で用いた MIKA 関連研専ネットワークのデータは匿名化した上で、MIKA_net.txt として置いている。
