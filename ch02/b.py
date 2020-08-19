n = int(input())
a = list(map(int,input().split()))
cnt =0
for i in range(n):
    minj = i
    for j in range(i,n):
        if a[minj]>a[j]:
            minj = j
    if minj != i:
        cnt += 1
    a[minj],a[i] = a[i],a[minj]
print(*a)
print(cnt)