# ネットワーク上のウィルス拡散
## Usage
ネットワーク上での SIR モデルのシミュレーションを一回試行するには以下のようにプログラムを実行します。
```bash
python3 sir.py network/er.txt
```
これを100回試行して、時刻ごとの感染経験のあるノード数の平均を出力するには以下のように実行します。
```bash
sh bin/run-sir.sh network/er.txt
```
