# Search key Element in BST:
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def search(root,key):
    if root is None:
        return False
    if root.data ==key:
        return True
    elif root.data>key:
        return search(root.left,key)
    else:
        return search(root.right,key)
    
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(search(root,key=3))

# print path of a Tree:
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def print_path(root,path=[]):
    if root is None:
        return
    path.append(str(root.data))
    if root.left is None and root.left is None:
        print(" ".join(path))
    else:
        print_path(root.left,path)
        print_path(root.right,path)
    path.pop()
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print_path(root)


#INTRODUCTION TO GRAPHS:

#A graph is a non-linear data structure consisting of nodes (vertices) and edges.
#It is widely used to represent networks like social media connections, road maps, and communication networks.
#Types of Graphs:
#1.Directed Graph(Digraph): Edges have a direction (one-way connection).
#2.Undirected Graph: Edges have no direction (bi-directional connection).
#3.Weighted Graph: Edges have associated weights (e.g., road distances).
#4.Unweighted Graph: Edges do not have weights.
#5.Cyclic Graph: Contains at least one cycle.
#6.Acyclic Graph: No cycles exist.
#7.Connected Graph: All nodes are reachable from any other node.
#8.Disconnected Graph: Some nodes are not reachable from others.

#Graph can be Represented in Two-ways:
#1.Adjacency List
#2.Adjacency Matrix


# DFS OF A GRAPH:
def dfs(graph,n,visited=set()):
    if n not in visited:
        print(n,end=" ")
        visited.add(n)
        for i in graph[n]:
            dfs(graph,i,visited)
            
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['D','E']
}
dfs(graph,n='A')
    

# BFS OF A GRAPH:
def BFS(graph,start):
    visited=set()
    q=[start]
    while q:
        n=q.pop(0)
        if n not in visited:
            print(n,end=" ")
            visited.add(n)
            q.extend(graph[n])

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['D','E']
}
BFS(graph,start='A')

#Directed Graph
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
def path(graph,start,end):
    visited=set()
    def dfs(val):
        if val==end:
            return True
        visited.add(val)
        for n in graph[val]:
            if n not in visited:
                if dfs(n):
                    return True
        return False
    return dfs(start)
  
start,end=0,5
print(path(graph,start,end))


#graph list:
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
def path(start,end,p=[]):
    p.append(start)
    if start==end:
        print(p)
    else:
        for n in graph[start]:
            if n not in p:
                path(n,end,p)
    p.pop()
start,end=0,5
path(start,end)

# path count of Graph:

from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u, v in edges:
    graph[u].append(v)
def count_paths(start,end,p=[],path_count=[0]):
    p.append(start)
    if start==end:
        path_count[0]+=1
    else:
        for n in graph[start]:
            if n not in p:
                count_paths(n,end,p,path_count)
    p.pop()
    return path_count[0]
path_count = 0
print(count_paths(0, 5))





