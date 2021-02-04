n,m=map(int,input().split())
adj_list=[[]for i in range(n+1)]
for _ in range(m):
    t_n,t_m=map(int,input().split())
    adj_list[t_n].append(t_m)
    if t_n not in adj_list[t_m]:
        adj_list[t_m].append(t_n)

colour=[-1 for i in range(n+1)]
def CFS(adj_list):
    for i in range(1,n+1):
        if colour[i]==-1:
            colour[i]=0
            for j in adj_list[i]:
                if colour[j]==-1:
                    colour[j]=1
                elif colour[j]==colour[i]:
                    return 0
        else:
            for j in adj_list[i]:
                if colour[j]==-1:
                    colour[j]=not colour[i]
                elif colour[i]==colour[j]:
                    return 0
    return 1
print(CFS(adj_list))
