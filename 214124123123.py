import pandas as pd
import io
import networkx as nx

data = """Source,Target,Type,Weight
1,2,undirected,3
1,3,undirected,3
1,4,undirected,6
1,5,undirected,3
1,6,undirected,5
1,7,undirected,6
1,8,undirected,3
1,9,undirected,5
1,10,undirected,3
1,11,undirected,3
1,12,undirected,3
1,13,undirected,3
1,14,undirected,6
2,3,undirected,3
2,4,undirected,6
2,5,undirected,2
2,6,undirected,6
2,7,undirected,4
2,8,undirected,4
2,9,undirected,4
2,10,undirected,4
2,11,undirected,6
2,12,undirected,6
2,13,undirected,6
2,14,undirected,6
3,4,undirected,6
3,5,undirected,3
3,6,undirected,5
3,7,undirected,5
3,8,undirected,4
3,9,undirected,4
3,10,undirected,4
3,11,undirected,3
3,12,undirected,3
3,13,undirected,3
3,14,undirected,6
4,5,undirected,6
4,6,undirected,6
4,7,undirected,6
4,8,undirected,6
4,9,undirected,6
4,10,undirected,6
4,11,undirected,6
4,12,undirected,6
4,13,undirected,6
4,14,undirected,6
5,6,undirected,3
5,7,undirected,4
5,8,undirected,4
5,9,undirected,4
5,10,undirected,4
5,11,undirected,3
5,12,undirected,3
5,13,undirected,3
5,14,undirected,6
6,7,undirected,4
6,8,undirected,4
6,9,undirected,4
6,10,undirected,4
6,11,undirected,3
6,12,undirected,3
6,13,undirected,3
6,14,undirected,6
7,8,undirected,2
7,9,undirected,3
7,10,undirected,2
7,11,undirected,3
7,12,undirected,3
7,13,undirected,3
7,14,undirected,6
8,9,undirected,3
8,10,undirected,2
8,11,undirected,3
8,12,undirected,2
8,13,undirected,3
8,14,undirected,6
9,10,undirected,1
9,11,undirected,3
9,12,undirected,3
9,13,undirected,3
9,14,undirected,6
10,11,undirected,3
10,12,undirected,3
10,13,undirected,3
10,14,undirected,6
11,12,undirected,1
11,13,undirected,1
11,14,undirected,6
12,13,undirected,2
12,14,undirected,6
13,14,undirected,6
"""
edges = pd.read_csv(io.StringIO(data))
# Build undirected graph
G = nx.Graph()
for _, row in edges.iterrows():
    G.add_edge(int(row.Source), int(row.Target), weight=row.Weight)
# Compute MST minimal sum of weights
mst = nx.minimum_spanning_tree(G, weight="weight")
# Prepare CSV lines
mst_edges = []
for u,v,data in mst.edges(data=True):
    w = data['weight']
    mst_edges.append((u,v,"undirected",int(w)))
mst_df = pd.DataFrame(mst_edges, columns=["Source","Target","Type","Weight"])
mst_df