import heapq as h
def algo(adj_list,u,v,heap,d):
    visit=[0 for _ in range(n+1)]
    dist=[float("inf") for _ in range(n+1)]
    dist[u]=0
    while heap:
        temp,t=h.heappop(heap)
        visit[t]=1
        for i in adj_list[t]:
            #print(d[(t,i)])
            if dist[t]+d[(t,i)]<dist[i]:
                dist[i]=dist[t]+d[(t,i)]
                h.heappush(heap,(dist[i],i))
    if dist[v]==float("inf"):
        return -1
    return dist[v]

n,m=map(int,input().split())
adj_list=[[] for i in range(n+1)]
d={}
for _ in range(m):
    i,j,dis=map(int,input().split())
    adj_list[i].append(j)
    d[(i,j)]=dis
s,e=map(int,input().split())
heap=[(float("inf"),i) for i in range(n+1)]
heap[s]=(0,s)
h.heapify(heap)
print(algo(adj_list,s,e,heap,d))
