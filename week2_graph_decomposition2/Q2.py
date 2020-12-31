from collections import deque

def explore(v):
    global post
    VisList[v] = 1
    for w in AdjList[v]:
        if not VisList[w]:
            explore(w)
    post.appendleft(v)

def DFS(n):
    for v in range(1, n+1):
        if not VisList[v]:
            explore(v)


n, m = map(int, input().split())
AdjList = [[] for i in range(n + 1)]
VisList = [0 for i in range(n + 1)]
post = deque()
for _ in range(m):
    v, w = map(int, input().split())
    AdjList[v].append(w)
DFS(n)
print(*post)
