n = int(input())
x = list(map(int, input().split()))

cnt = 0

for i in range(n):
    minj = i
    j = i
    for j in range(i,n): #iからnまでまわす
        if x[j]<x[minj]: #iからnまでで最小になるminjをキメル
            minj = j
    x[i],x[minj] = x[minj],x[i]　#スワップする
    if i != minj:
        cnt += 1
print(' '.join([str(i) for i in x]))
print(cnt)
