n = int(input())
x = list(map(int,input().split()))

cnt =0
for i in range(n):
    for j in range(n):
        if j < n-1:
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
                cnt += 1

print(' '.join([str(i) for i in x]))
print(cnt)
        