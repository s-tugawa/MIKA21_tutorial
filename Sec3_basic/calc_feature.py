import sys
import networkx as nx
from numpy  import *
import numpy as np

import matplotlib.pyplot as plt

#ネットワークの読み込み
file=sys.argv[1]
#delimiter は区切り文字に合わせて変更する
G=nx.read_edgelist(file,nodetype=str,encoding='utf-8',delimiter="\t")


deg_seq = list(dict(G.degree()).values())
avedeg=np.average(deg_seq)

#ネットワークの基本的な特徴量を出力
print("num. nodes: "+str(len(G.nodes())))
print("num. edges: "+str(len(G.edges())))
print("average degree: "+str(avedeg))
print("density: "+str(nx.density(G)))
print("clustering coefficient: "+str(nx.average_clustering(G)))
print("degree assortativity: "+str(nx.degree_assortativity_coefficient(G)))
print("num. of. components: "+str(nx.number_connected_components(G)))

#最大連結成分の抽出
giant = max(nx.connected_components(G), key=len)
gc=G.subgraph(giant).copy()

frac=len(gc)/len(G.nodes())
print("frac. of GC: "+str(frac))
print("average shortest path length: "+str(nx.average_shortest_path_length(gc)))
print("diameter: "+str(nx.diameter(gc)))

#コミュニティの抽出とモジュラリティの計算
import networkx.algorithms.community as nx_comm
com=nx_comm.greedy_modularity_communities(gc)
print("num. communities: "+str(len(com)))
print("modularity: "+str(nx_comm.modularity(gc,com)))



# 次数分布を求める    
maxk = np.max(deg_seq)
ks= arange(0,maxk+1) 
prob = np.zeros(maxk+1) # P(k)
for k in deg_seq:
    prob[k] = prob[k] + 1
prob = prob/sum(prob)


# 次数分布を線形軸でプロットして保存
plt.figure()
plt.scatter(ks,prob)
plt.xlabel("Degree $k$", fontsize=15)
plt.ylabel("Probability $P(k)$", fontsize=15)
outfile="degree_dist_"+str(file)+".eps"
plt.savefig(outfile) 

# 次数分布を対数軸でプロットして保存
plt.loglog(ks,prob,"o")
plt.xlabel("Degree $k$", fontsize=15)
plt.ylabel("Probability $P(k)$", fontsize=15)
outfile="degree_dist_log_"+str(file)+".eps"
plt.savefig(outfile) 

