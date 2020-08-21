n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))

cnt = 0
check = []
for tnum in t:
    check.append(tnum)
    
    if tnum in s:
        cnt += 1
print(cnt)
        

    