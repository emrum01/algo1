5
1 1 2 2 3
2
1 n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int,input().split()))
cnt = 0
for key in t:
    r = n
    l = 0

    find = 0
    while l<r:
        m = (l+r)//2
        if key < s[m]:
            r = m   
        if key == s[m]:
            find = 1
            break
        if key > s[m]:
            l = m+1
    cnt += find

print(cnt)       

        