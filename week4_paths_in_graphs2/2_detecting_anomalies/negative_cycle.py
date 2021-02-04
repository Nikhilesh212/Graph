#Uses python3
n,m=map(int,input().split())
edge_list=[]
dist=[float("inf") for _ in range(n+1)]
for i in range(1,n+1):
    edge_list.append(((0,i),0))
dist[0]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    edge_list.append(((a,b),c))

for _ in range(n):
    for ((u,v),c) in (edge_list):
        if dist[v]>dist[u]+c:
            dist[v]=dist[u]+c
flag=0
for ((u,v),c) in (edge_list):
    if dist[v]>dist[u]+c:
        flag=1
        break
        dist[v]=dist[u]+c
print(flag)
