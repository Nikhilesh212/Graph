import sys
sys.setrecursionlimit(10**6)
def explore(v,AdjList):
    global post,VisList
    VisList[v] = 1
    for w in AdjList[v]:
        if not VisList[w]:
            explore(w,AdjList)
    post.append(v)


def DFS(n,Adj_List):
    for v in range(1, n+1):
        if not VisList[v]:
            explore(v,Adj_List)

def scc(post,Adj_List):
    global VisList,cc
    while post:
        node=post.pop()
        if not VisList[node]:
            explore(node,Adj_List)
            cc+=1

cc=0
n,m=map(int,input().split())
adj_list=[[]for i in range(n+1)]
adj_rev=[[]for i in range(n+1)]
for _ in range(m):
    t_n,t_m=map(int,input().split())
    adj_list[t_n].append(t_m)
    adj_rev[t_m].append(t_n)
VisList=[0]*(n+1)
post = []
DFS(n,adj_rev)
VisList=[0]*(n+1)
scc(post,adj_list)
print(cc)
