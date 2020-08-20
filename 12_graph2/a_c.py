from heapq import heappush, heappop, heapify

n = int(input())
g = [[] for _ in range(n)]

for i in range(n):
    for j,k in enumerate(map(int,input().split())):
        if k != -1:
            g[i].append((j,k))
#    print(g[i])

ocupied = [0]*n
que = [(j,k) for k,j in g[0]] # 重み、子の順番
#print(f'g[0]: {g[0]}')　#子、重みの順番
#print(f'que: {que}')
ocupied[0] = 1
heapify(que)

ans = 0
while que:
    cv,v = heappop(que)
    #print(f'cv, v: {cv}, {v}')
    if ocupied[v]: # vは頂点　どこでvが頂点になるか
        continue
    ocupied[v] = 1
    ans += cv
    for j,k in g[v]:
        if ocupied[j]:
            continue
        heappush(que,(k,j))
    #print(f'ocupied: {ocupied}')
print(ans)


