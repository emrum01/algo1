def countingSort(a,m):
    m += 100
    cnt = [0]*m
    for i in a:
        cnt[i] += 1
    i = 0
    for b in range(m):
        for c in range(cnt[b]):
            a[i] = b
            i+=1
    return a
n = int(input())
a = countingSort(list(map(int,input().split())),n)
print(*a)