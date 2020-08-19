def dfs(i,cnt):
    d[i] = cnt
    cnt += 1
    for j in edge[i]:
        if d[j] == -1:
            cnt = dfs(j,cnt)
    f[i] = cnt
    cnt += 1
    return cnt

n = int(input())
edge = [[] for i in range(n)]
for not_used in range(n):
    of_children, not_used, *v = map(lambda x: int(x)-1,input().split())
    edge[of_children] = sorted(v)
c = 1
d = [-1]*n
f = [-1]*n

for i in range(n):
    if d[i] == -1:
        c = dfs(i,c)
for i ,(d,f) in enumerate(zip(d,f))
    print(i+1,d,f)