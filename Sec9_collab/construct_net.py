import sys,os
import networkx as nx
#1行ずつ読んで改行を除去
def each_line(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\r\n')

list=sys.argv[1] #入力ファイル

# 著者の登場回数を数える
count={}
for line in each_line(list):
    authors=line.split(',')
    for i in authors:
        if i in count:
            count[i]+=1
        else:
            count[i]=1

g=nx.Graph()
for line in each_line(list):
    authors=line.split(',')
    while len(authors)>0:
        u=authors.pop(0)
        # 1回しか出てこない著者はネットワークに含めない
        if count[u]<=1:
            continue

        for v in authors:
            if count[v]<=1:
                continue
            if not g.has_edge(u,v):
                g.add_edge(u,v)

for e in g.edges():
    print(str(e[0])+","+str(e[1]))

