n = int(input())
a = list(input().split())
b = a[:]
for i in range(n):
    for j in range(n-1):
        if a[j][1]>a[j+1][1]:
            a[j],a[j+1] = a[j+1],a[j]
    minj = i
    for j in range(i,n):
        if b[minj][1]>b[j][1]:
            minj = j
    b[minj],b[i] = b[i],b[minj]        
print(*a)
print('Stable')
print(*b)
print(['Not s','S'][a==b] + 'table')


