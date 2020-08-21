n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))


cnt = 0
for tnum in t: 
    find = 0
    l = 0
    r = n
    while l<r:
        m = (l+r)//2
        if s[m] != tnum:
            if s[m]<tnum:
                l = m+1
            elif tnum < s[m]:
                r = m
        elif s[m] == tnum:
            find = 1
            break
    cnt += find
print(cnt)

