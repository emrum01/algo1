n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            cnt += 1
print(*a)
print(cnt)