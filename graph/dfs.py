# https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python
from collections import defaultdict

def dfs(graph,node,visited):
    # if the node is visited then just return
    print(node,visited)
    if node not in visited:
        visited.add(node)
        for vert in graph[node]:
            dfs(graph,vert,visited)
    return visited

def bfs(graph,node,visited):
    queue = [node]
    visited = {node}
    while queue:
        vertex = queue.pop(0)
        for nei in graph[vertex]:
            if nei not in visited:
                queue.append(nei) 
    return visited 
                 

def createGraph(edges):
    graph = defaultdict(list)
    # undirected graph so insert the edge in both nodes
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph 


if __name__ == "__main__":
    edges = [[1,2],[1,3],[2,4],[3,5],[4,5]]
    graph = createGraph(edges)
    print(graph)
    print(dfs(graph,4,set()))
