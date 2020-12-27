n,m=map(int,input().split())
visit=[0]*(n+1)
def visit_graph(i,l):
    visit[i]=1
    for j in l[i]:
        if visit[j]==0:
            visit_graph(j,l)
adj_list=[[]for i in range(n+1)]
for _ in range(m):
    t_n,t_m=map(int,input().split())
    adj_list[t_n].append(t_m)
    if t_n not in adj_list[t_m]:
        adj_list[t_m].append(t_n)
t_n,t_m=map(int,input().split())
visit_graph(t_n,adj_list)
if visit[t_m]:
    print(1)
else:
    print(0)
