import heapq
from math import sqrt as sq
from random import randint as r

def w(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return sq((x2-x1)**2 + (y2-y1)**2)

def Prim(l):
    cost = [float('inf') for _ in range(n)]
    u = r(0, n-1)
    cost[u] = 0
    Q = [(float('inf'), i) for i in range(n)]
    q = {(float('inf'), i):False for i in range(n)}
    Q[u] = (0, u)
    heapq.heapify(Q)
    while Q:
        d, pt1 = heapq.heappop(Q)
        q[(d,pt1)] = True
        for pt2 in range(n):
            if pt2 == pt1:
                continue
            if not q[(cost[pt2], pt2)] and cost[pt2] > w(l[pt1], l[pt2]):
                cost[pt2] = w(l[pt1], l[pt2])
                heapq.heappush(Q, (cost[pt2], pt2))
                q[(cost[pt2], pt2)] = False

    return sum(cost)

n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
print(Prim(l))
