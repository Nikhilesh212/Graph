#Uses python3
import sys
import math
l=[]
for _ in range(int(input())):
    l.append(list(map(int,input().split())))

adj_list=[[]for _ in range(n+1)]
for i in range(1,n):
    for j in range(i+1,n+1):
        t=math.sqrt((l[i-1][0]-l[j-1][0])**2+(l[i-1][1]-l[j-1][1])**2)
        print(t)
        adj_list[i].append((j,t))
        adj_list[j].append((i,t))


def prim(adj_list):
    dist    =[float("inf") for _ in range(n+1)]
    dist[1]=0
    q=heappify()
    while q:
        v=heapq.pop(q)
        for adj_list
