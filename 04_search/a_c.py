n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int,input().split()))

cnt = 0

for i in t:
    find = 0
    for j in s:
        if j==i:
            find = 1
    cnt += find
        
print(cnt)