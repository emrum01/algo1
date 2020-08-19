#挿入ソートとは左端の数値を起点として一つ右の数との大小を比べて並び替えるもの

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    j = i
    while j>0:
        if a[j]<a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            j-=1
        else:
            j-=1
            continue
    print(' '.join(str(i) for i in a))

