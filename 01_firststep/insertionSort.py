n = int(input())
a = list(map(int,input().split()))
print(*a)
for i in range(n-1):
    j = i
    while j>=0 and a[j]>a[j+1]:
        a[j],a[j+1] = a[j+1],a[j]
        j-=1
    print(*a)