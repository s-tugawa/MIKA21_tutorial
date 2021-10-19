from numpy.random import *
import sys, os, os.path
from networkx import *

# ネットワークの読み込み
g=read_edgelist(sys.argv[1])

# model parameters
beta=0.04 # infection rate
r=0.2 #recovery rate

inf={} #感染ノードを管理する辞書
# ランダムに選んだノードを1つ状態 I にする
i = choice(list(g.nodes()))
inf[i]=1

max_count = 100
num_r=0
for time in range(1,max_count):
    inflist=list(inf.keys())
    shuffle(inflist)
    for v in inflist:
        for nbr in g[v]:
            if nbr not in inf:
                if (random()<beta):
                    inf[nbr]=1
        if(random()<r):
            del inf[v]
            g.remove_node(v)
            num_r+=1
    num_inf=num_r+len(inf)
    # 時刻、状態 S の数、Iの数、Rの数、R+I の数
    print(time,len(g.nodes()),len(inf),num_r,num_inf)
#    if len(inf)==0:
#        break




            
