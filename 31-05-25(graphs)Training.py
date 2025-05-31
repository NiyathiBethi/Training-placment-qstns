# 997. Find the Town Judge--- LEET CODE

class Solution:
    def findJudge(self,n:int,trust:List[List[int]]) -> int:
        if n==1:
            return 1
        d=collections.defaultdict(list)
        for i,j in trust:
            d[i].append(j)
            d[j]
        for i in d:
          if len(d[i])==0:
                j=i
                break
        else:
            return -1
        for i in d:
            if j not in d[i] and i!=j:
                return -1
        return j
    
# 547. Number of Provinces-- LEET CODE

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
          return 0
        n=len(isConnected)
        visited=[0]*n
        def dfs(node):
          for ne in range(n):
           if isConnected[node][ne]==1 and not visited[ne]:
              visited[ne]=1
              dfs(ne)
        count=0
        for i in range(n):
          if not visited[i]:
            visited[i]=1
            count+=1
            dfs(i)
        return count
    
# COUNT ALL THE PATHS OF THE GRAPH

from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
def path_count(start,end,p=None,c=0):
    if p is None:
        p=[]
    p.append(str(start))
    if start==end:
        print(p)
        c+=1
    else:
        for i in graph[start]:
            if i not in p:
                c=path_count(i,end,p,c)
    p.pop()
    return c
start,end=0,5
print(path_count(start,end))

#CHECK WEATHER A GRAPH IS HAVING CYCLE OR NOT

def cycle(graph):
    visited=[False]*(len(graph))
    for n in range(len(graph)):
        if not visited[n]:
            q=[(n,-1)]
            while q:
                node,prev=q.pop(0)
                visited[node]=True
                for ne in graph[node]:
                    if not visited[ne]:
                        q.append((ne,node))
                    elif ne!=prev:
                        return True
    return False 
list=[[1],[0,2,3],[1,3],[1,2]]
print(cycle(list))