n,m=map(int,input().split())

adj_list=[[]for i in range(n+1)]
for _ in range(m):
    t_n,t_m=map(int,input().split())
    adj_list[t_n].append(t_m)

def visit(i,l,c,v):
    global ans
    v[i]=1
    for j in l[i]:
        if j==c:
            ans = 1
        if v[j]==0:
            visit(j,l,c,v)

def cycle(adj_list,n):
    for i in range(1,n+1):
        v=[0 for _ in range(n+1)]
        visit(i,adj_list,i,v)

ans=0
cycle(adj_list,n)
print(ans)
