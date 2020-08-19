from heapq import heapify heappop heappush

n = int(input())
g = [[] for _ in range(n)]

ocupied = [0]*n

for w,c in enumerate(map(int,input().split())):
    if c != -1:
        g.append((w,c))

que = [(c,w) for w,c in g[0]]
heapify(que)
ans = 0
ocupied[0]=1

while que:
    cv, v = heappop(que)
    if ocupied[v]==1
        continue
    ocupied[v] = 1
    ans += cv
    for c,w in g[v]:
        if ocupied[c]:
            continue
        heappush(que,(w,c))
print(ans)



    