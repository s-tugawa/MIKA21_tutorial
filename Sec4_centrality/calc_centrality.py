import sys
import networkx as nx

input=sys.argv[1]
g=nx.read_edgelist(input,create_using=nx.DiGraph)

#入次数
indeg=nx.in_degree_centrality(g)
#出次数
outdeg=nx.out_degree_centrality(g)
#媒介中心性
bet=nx.betweenness_centrality(g)
#近接中心性
clo=nx.closeness_centrality(g)
#PageRank
pr = nx.pagerank(g)
#コアネス
kcore=nx.core_number(g)
for v in g.nodes():
    print(v,indeg[v],outdeg[v],bet[v],clo[v],pr[v],kcore[v])
