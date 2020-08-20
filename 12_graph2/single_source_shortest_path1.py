from heapq import heappush, heappop
import math
def dijkstra(N, G, s):
    dist = [math.inf] * N
    que = [(0,s)]
    dist[s] = 0
    ans = [[] for i in range(N)]
    while que:
        c,v = heappop(que)
        if dist[v] < c:
            
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que,(dist[t],t))
    return dist
n = int(input())

g = [[]for i in range(n)]
for i in range(n):
    nums=list(map(int,input().split()))
    node=nums[0]
    for j in range(nums[1]):
        t=nums[j*2+2]
        c=nums[j*2+3]
        g[node].append([t,c])
   
ans = dijkstra(n,g,0)
for i in range(n):
    print(f'{i} {ans[i]}')

        
