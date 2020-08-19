def partition(a,p,r):
    x = a[r]
    i = p
    for j in range(p,r):
        if x>=a[j]:
            a[i],a[j] = a[j],a[i]
            i+=1
    a[r],a[i] = a[i],a[r]
    return i

n = int(input())
a = list(map(int,input().split()))

m = partition(a,0,n-1)
print(' '.join(map(str,a[0:m]))+' ['+str(a[m])+'] ' +' '.join(map(str,a[m+1:])))