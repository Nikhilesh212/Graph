cc=1
n,m=map(int,input().split())
visit=[0]*(n+1)

def visit_graph(i,l):
    global cc
    if not visit[i]:
        visit[i]=cc
        for j in l[i]:
            if visit[j]==0:
                visit_graph(j,l)


def no_island(l):
    for i in range(1,len(l)):
        if not visit[i]:
            visit_graph(i,l)
            global cc
            cc+=1


adj_list=[[]for i in range(n+1)]
for _ in range(m):
    t_n,t_m=map(int,input().split())
    adj_list[t_n].append(t_m)
    if t_n not in adj_list[t_m]:
        adj_list[t_m].append(t_n)
no_island(adj_list)
print(max(visit))
