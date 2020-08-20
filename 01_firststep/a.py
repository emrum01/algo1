n = int(input())
a = list(map(int,input().split()))

print(*a)
for i in range(n-1):
    j = i
    while a[j]>a[j+1] and j>=0:
        a[j],a[j+1] = a[j+1],a[j]
        j -= 1
    print(*a)