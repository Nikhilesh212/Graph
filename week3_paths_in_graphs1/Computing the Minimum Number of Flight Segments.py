from collections import deque
n,m=map(int,input().split())
adj_list=[[]for i in range(n+1)]
for _ in range(m):
    t_n,t_m=map(int,input().split())
    adj_list[t_n].append(t_m)
    if t_n not in adj_list[t_m]:
        adj_list[t_m].append(t_n)
        
v,u=map(int,input().split())
Q=deque()
dist=[-1 for i in range(n+1)]
def bfs(adj_list,v,u):
    dist[v]=0
    Q.append(v)
    while Q:
        temp=Q.popleft()
        for i in adj_list[temp]:
            if dist[i]==-1:
                Q.append(i)
                dist[i]=dist[temp]+1
bfs(adj_list,v,u)
print(dist[u])
