# コミュニティ抽出
## Usage
空手クラブのネットワークにGirvan-Newman法を適用してコミュニティを抽出するには、以下のようにプログラムを実行します。
```bash
python3 community_karate.py
```
Email のネットワークのコミュニティを抽出し、所属のラベルと比較して RandIndex を計算するには、以下のようにプログラムを実行します。
```bash
python3 community_email.py email-Eu-core.txt email-Eu-core-department-labels.txt
```
データは、以下から入手してください。
http://snap.stanford.edu/data/email-Eu-core.html

## 練習問題
様々なネットワークのコミュニティを抽出し、その結果を可視化してみよう。
- http://snap.stanford.edu/data/index.html
- http://networksciencebook.com/translations/en/resources/data.html
