import sys
from networkx import *
import numpy as np

input=sys.argv[1]
g=read_edgelist(input)

n=len(g.nodes())

giant = max(nx.connected_components(g), key=len)
removed=0
while(len(giant)>1):
    deg=dict(g.degree())
    max_v = max(deg, key=deg.get)
    g.remove_node(max_v)
    removed+=1
    if (removed % 10)==0:
        giant = max(nx.connected_components(g), key=len)
        f_gc=len(giant)/n
        f_removed=removed/n
        print(f_removed,f_gc)
        if(len(giant)<10):
            break








