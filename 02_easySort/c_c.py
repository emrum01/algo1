n=int(input())
b=input().split()
s=b[:]
for i in range(n):
    for j in range(n-1):
        if b[j][1]>b[j+1][1]:
            b[j],b[j+1]=b[j+1],b[j]
    minj=i
    for j in range(i,n):
        if s[minj][1]>s[j][1]:
            minj=j
    s[minj],s[i]=s[i],s[minj]
print(*b)
print('Stable')
print(*s)
print(['Not s','S'][b==s]+'table')