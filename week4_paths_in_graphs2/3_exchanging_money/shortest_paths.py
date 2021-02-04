from collections import deque

def explore(adjlist,s,visit,dist):
    visit[s]=1
    dist[s]=-float("inf")
    for (i,j) in adjlist[s]:
        if not visit[i]:
            explore(adjlist,i,visit,dist)

def BellmanFord(adjlist,dist,s,n):
    for i in range(n):
        for u in range(n+1):
            for (v,w) in adjlist[u]:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
    neg_cycle=[]
    for u in range(n+1):
        for (v,w) in adjlist[u]:
            if dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
                neg_cycle.append(v)

    return neg_cycle

n,m=map(int,input().split())
adjlist=[[]for _ in range(n+1)]

for _ in range(m):
    u,v,w=map(int,input().split())
    adjlist[u].append((v,w))

s=int(input())
dist=[float("inf") for _  in range(n+1)]
dist[s]=0
visit=[0 for _ in range(n+1)]
cycle=BellmanFord(adjlist,dist,s,n)
for i in cycle:
    explore(adjlist,i,visit,dist)

for i in range(1,n+1):
    if dist[i]==float("inf"):
        print("*")
    elif dist[i]==-float("inf"):
        print("-")
    else:
        print(dist[i])
