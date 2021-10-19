import sys
from networkx import *
import numpy as np

#データ読み込み
input=sys.argv[1]
g=read_edgelist(input)

n=len(g.nodes())
#最大連結成分の取得
giant = max(nx.connected_components(g), key=len)
removed=0
deg=dict(g.degree())
#次数の高い順にループ
for v, k in sorted(deg.items(), key=lambda x: -x[1]):
    g.remove_node(v)
    removed+=1
    if (removed % 10)==0:
        giant = max(nx.connected_components(g), key=len)
        f_gc=len(giant)/n
        f_removed=removed/n
        print(f_removed,f_gc)
        if(len(giant)<=10):
            break





